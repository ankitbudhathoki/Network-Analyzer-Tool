

## *Network Traffic Analyzer*

A simple Python-based tool to sniff, log, and analyze network traffic, with real-time packet capture, data visualization, and an optional GUI using Streamlit.

---

### *Features*
- Live packet sniffing using Scapy
- Logs source IP, destination IP, and protocol
- Analyzes protocol distribution and top IPs
- Generates visual graphs using Matplotlib
- Interactive dashboard built with Streamlit
- Bash script to automate the workflow

---

### *Screenshots*

![image](https://github.com/user-attachments/assets/78dcfba4-683e-4405-ba67-c34b00c172b5)

![image](https://github.com/user-attachments/assets/13be1133-e491-420e-8717-74e4c8468c06)



---

### *Tech Stack*
- *Python 3*
- *Scapy* – for packet sniffing
- *Pandas* – for data handling
- *Matplotlib* – for plotting
- *Streamlit* – for GUI
- *Bash* – for automation

---

### *Installation*

#### Clone the repo:
```bash
git clone https://github.com/yourusername/network-traffic-analyzer.git
cd network-traffic-analyzer
```


#### Install dependencies:
```bash
pip install -r requirements.txt
```

> If using a Linux system with an “externally managed environment,” use:
```bash
pip install -r requirements.txt --break-system-packages
```

#### (Optional) Create a virtual environment:
```bash
python3 -m venv env
source env/bin/activate
```

---

### *Usage*

Run the analyzer with the bash script:

```bash
chmod +x run-analyzer.sh
./run-analyzer.sh
```

It will:
1. Capture 1000 packets
2. Save them to packet_log.csv
3. Analyze and generate graphs
4. Optionally launch the Streamlit GUI

---

### *File Structure*
```
├── packet_sniffer.py
├── analyze_traffic.py
├── gui.py
├── run-analyzer.sh
├── packet_log.csv (auto-generated)
├── protocol_distribution.png (auto-generated)
```

---

### *Known Issues*
- Streamlit may require setting PATH manually (~/.local/bin)
- GUI plotting may fail without tkinter; use Agg backend to save plots

---

### *To Do / Improvements*
- Real-time Streamlit dashboard
- Port scan detection
- Email alert system for suspicious traffic

---

### *License*
This project is licensed under the MIT License.

---

