#!/bin/bash
export PATH=$PATH:/home/**Your Username**/.local/bin

echo "=== Network Traffic Analyzer ==="

# Run packet capture with sudo
echo "[+] Starting packet capture (100 packets)..."
sudo python3 packet-sniffer.py

# Check if capture was successful
if [ -f "packet_log.csv" ]; then
    echo "[+] Packet capture complete."
else
    echo "[!] Failed to capture packets. Exiting."
    exit 1
fi

# Run analysis
echo "[+] Running traffic analysis..."
python3 analyze-traffic.py

# Ask if user wants to launch GUI
read -p "Do you want to launch the GUI (Streamlit)? (y/n): " choice
if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
    echo "[+] Launching GUI..."
    streamlit run gui.py
else
    echo "[+] Done. GUI skipped."
fi
