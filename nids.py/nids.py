from scapy.all import sniff, IP, TCP, ICMP
from collections import defaultdict
import time

syn_count = defaultdict(int)
icmp_count = defaultdict(int)

SYN_THRESHOLD = 10
ICMP_THRESHOLD = 10

LOG_FILE = "nids_alerts.log"

def log_alert(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    alert_message = f"[{timestamp}] {message}"
    
    print("ALERT:", alert_message)
    
    with open(LOG_FILE, "a") as f:
        f.write(alert_message + "\n")

def detect_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        
        if packet.haslayer(TCP):
            if packet[TCP].flags == "S":
                syn_count[src_ip] += 1
                if syn_count[src_ip] > SYN_THRESHOLD:
                    log_alert(f"Possible SYN Flood from {src_ip}")
                    syn_count[src_ip] = 0

        if packet.haslayer(ICMP):
            icmp_count[src_ip] += 1
            if icmp_count[src_ip] > ICMP_THRESHOLD:
                log_alert(f"Possible ICMP Flood from {src_ip}")
                icmp_count[src_ip] = 0

        if packet.haslayer(TCP):
            dport = packet[TCP].dport
            sensitive_ports = [21, 22, 23, 3389]
            
            if dport in sensitive_ports:
                log_alert(f"Access to sensitive port {dport} from {src_ip}")

if __name__ == "__main__":
    print("Simple NIDS Started... Press Ctrl+C to stop")
    sniff(filter="ip", prn=detect_packet, store=False)