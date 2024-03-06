import tkinter as tk
from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urllib.parse
from collections import deque
import re
import lxml


def scan_website():
    user_url = url_entry.get()
    urls = deque([user_url])
    scrapped_url = set()
    emails = set()
    ip_addresses = set()  # To store IP addresses
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
            status_label.config(text='Processing %d: %s' % (count, url))
            try:
                response = requests.get(url)
                new_emails = set(re.findall(r'[a-z0-9\. \-+_]+@[a-z0-9\. \-+_]+\.[com]+', response.text, re.I))
                emails.update(new_emails)

                soup = BeautifulSoup(response.text, features="lxml")

                # Find IPv4 addresses using regex
                ipv4_addresses = set(re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', response.text))
                ip_addresses.update(ipv4_addresses)

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
        status_label.config(text='Closing!')

    # Display found emails, IP addresses, and phone numbers
    for mail in emails:
        result_text.insert(tk.END, mail + '\n')
    for ip in ip_addresses:
        result_text.insert(tk.END, ip + '\n')
    for phone in phone_numbers:
        result_text.insert(tk.END, phone + '\n')


# Create tkinter window
window = tk.Tk()
window.title("Web Hunter -by Devil")

# URL Entry
url_label = tk.Label(window, text="Enter Target URL to scan:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Scan Button
scan_button = tk.Button(window, text="Scan Website", command=scan_website)
scan_button.pack()

# Status Label
status_label = tk.Label(window, text="")
status_label.pack()

# Result Textbox
result_text = tk.Text(window, width=80, height=20)
result_text.pack()

window.mainloop()
