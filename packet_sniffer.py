from scapy.all import sniff, IP
import pandas as pd

packet_log = []

def packet_callback(packet):
    if IP in packet:
        packet_log.append({
            "source": packet[IP].src,
            "destination": packet[IP].dst,
            "protocol": packet[IP].proto
        })

print("Sniffing packets... (Capturing 1000 packets)")
sniff(prn=packet_callback, count=1000)  # You can change count or add a timeout

# Save to CSV
df = pd.DataFrame(packet_log)
df.to_csv("packet_log.csv", index=False)
print("Captured packets saved to packet_log.csv")
