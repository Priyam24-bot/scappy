# 🚨 Network Intrusion Detection System (NIDS) using Scapy

## 📌 Overview

This project is a **basic Network Intrusion Detection System (NIDS)** built using Python and Scapy.
It captures live network traffic and detects suspicious activities like:

* SYN Flood Attacks
* ICMP Flood Attacks
* Access to Sensitive Ports

The system generates real-time alerts in the terminal and logs them into a file.

---

## 🎯 Objectives

* Monitor real-time network traffic
* Detect common network attacks
* Generate alerts for suspicious activities
* Understand working of intrusion detection systems

---

## 🛠️ Technologies Used

* Python
* Scapy
* Collections (defaultdict)
* Time module

---

## ⚙️ How It Works

### 1️⃣ Packet Capture

The system uses Scapy to sniff live network packets:

```python
sniff(filter="ip", prn=detect_packet, store=False)
```

---

### 2️⃣ Detection Logic

#### 🔹 SYN Flood Detection

* Counts TCP SYN packets from each IP
* If threshold exceeds → Alert generated

#### 🔹 ICMP Flood Detection

* Counts ICMP (ping) packets
* Detects abnormal traffic

#### 🔹 Sensitive Port Monitoring

Monitors access to:

* 21 (FTP)
* 22 (SSH)
* 23 (Telnet)
* 3389 (RDP)

---

### 3️⃣ Alert System

* Displays alerts in terminal
* Saves alerts in `nids_alerts.log` file

Example:

```
ALERT: Possible SYN Flood from 192.168.1.10
```

---

## ▶️ How to Run

### Step 1: Install Dependencies

```bash
pip install scapy
```

### Step 2: Run the Script

```bash
python nids.py
```

---

## 🧪 Testing the System

### Generate ICMP Traffic:

```bash
ping 127.0.0.1
```

### For Quick Alerts (Optional):

Lower thresholds in code:

```python
SYN_THRESHOLD = 2
ICMP_THRESHOLD = 2
```

---

## 📁 Project Structure

```
├── nids.py
├── nids_alerts.log
├── README.md
```

---

## 📊 Sample Output

```
Simple NIDS Started... Press Ctrl+C to stop
ALERT: Possible SYN Flood from 172.16.x.x
```

---

## ⚠️ Limitations

* Basic detection only (no deep packet inspection)
* May generate false positives
* No GUI or dashboard
* Works best for learning/demo purposes

---

## 🚀 Future Improvements

* Web dashboard using Flask
* GUI using Tkinter
* Machine Learning-based detection
* Auto IP blocking system
* Real-time graphs

---

## 🧠 Learning Outcome

This project helps understand:

* Packet sniffing
* Network protocols (TCP, ICMP)
* Basic intrusion detection logic
* Real-time monitoring systems

---

## 🔐 Real-World Tools

This project is inspired by real IDS tools like:

* Snort
* Suricata

---

## 👨‍💻 Author

**Priyam Srivastava**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
