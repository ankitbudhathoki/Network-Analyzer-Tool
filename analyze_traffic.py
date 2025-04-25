import pandas as pd
import matplotlib.pyplot as plt

# Load the captured data
df = pd.read_csv("packet_log.csv")

print("=== Sample Data ===")
print(df.head())

# Analyze protocol usage
print("\n=== Protocol Usage ===")
print(df['protocol'].value_counts())

# Analyze top source IPs
print("\n=== Top Source IPs ===")
print(df['source'].value_counts().head(5))

# Plot protocol distribution
df['protocol'].value_counts().plot(kind='bar', title='Protocol Distribution')
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.tight_layout()
plt.show()
