import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
import sqlite3
import lxml


class PhoneNumber:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800+0+0")
        self.root.title("Phone")

        # URL Entry
        self.url_label = tk.Label(text="Enter Target URL to scan:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # Scan Button
        self.scan_button = tk.Button(root, text="Scan Website", command=self.scan_website)
        self.scan_button.pack()

        # Status Label
        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

        # Result Textbox
        self.result_text = tk.Text(root, width=80, height=20)
        self.result_text.pack()

    def scan_website(self):
        user_url = self.url_entry.get()
        urls = deque([user_url])
        scrapped_url = set()
        phone_numbers = set()  # To store phone numbers

        count = 0
        try:
            while len(urls):
                count += 1
                if count == 100:
                    break
                url = urls.popleft()
                scrapped_url.add(url)

                parts = urllib.parse.urlsplit(url)
                base_url = '{0.scheme}://{0.netloc}'.format(parts)

                path = url[:url.rfind('/') + 1] if '/' in parts.path else url
                self.status_label.config(text='Processing %d: %s' % (count, url))
                try:
                    response = requests.get(url)

                    soup = BeautifulSoup(response.text, features="lxml")

                    # Find phone numbers using regex
                    # Common formats: (XXX) XXX-XXXX, XXX-XXX-XXXX, XXX.XXX.XXXX
                    new_phone_numbers = set(re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', response.text))
                    phone_numbers.update(new_phone_numbers)

                    for anchor in soup.find_all("a"):
                        link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
                        if link.startswith('/'):
                            link = base_url + link
                        elif not link.startswith('http'):
                            link = path + link
                        if link not in urls and link not in scrapped_url:
                            urls.append(link)

                except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                    continue

        except KeyboardInterrupt:
            self.status_label.config(text='Closing!')

        # Display found emails, IP addresses, and phone numbers
        lsnum = []
        for phone in phone_numbers:
            lsnum.append(phone)
            self.result_text.insert(tk.END, phone + '\n')

        # Connect to the database
        con = sqlite3.connect("WEB_HUNTER.db")
        cur = con.cursor()

        # Define the SQL statement with parameterized query
        q = "INSERT INTO ph_number (no, ph_no) VALUES (?,?)"

        # Iterate over the list of phone numbers and insert them into the database
        count = 1
        for val in lsnum:
            cur.execute(q, (count, val))  # Execute the parameterized query with the count and phone number
            count += 1

        # Commit the transaction and close the connection
        con.commit()
        con.close()


if __name__ == "__main__":
    root = Tk()
    obj = PhoneNumber(root)
    root.mainloop()
