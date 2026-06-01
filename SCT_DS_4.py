import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("US_Accidents_March23.csv", low_memory=False)

print("Shape:", df.shape)
print("\nMissing values (top 10):\n", df.isnull().sum().sort_values(ascending=False).head(10))

df = df.dropna(subset=["Start_Lat", "Start_Lng", "Severity", "Weather_Condition", "Sunrise_Sunset"])
df["Start_Time"] = pd.to_datetime(df["Start_Time"], errors="coerce")
df = df.dropna(subset=["Start_Time"])
df["Hour"] = df["Start_Time"].dt.hour
df["Month"] = df["Start_Time"].dt.month
df["DayOfWeek"] = df["Start_Time"].dt.day_name()

day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

fig, axes = plt.subplots(2, 3, figsize=(20, 13))
fig.suptitle("US Traffic Accidents Analysis (2016–2023)", fontsize=16, fontweight="bold", y=1.01)

severity_counts = df["Severity"].value_counts().sort_index()
colors_sev = ["#81C784", "#FFD54F", "#FF8A65", "#E53935"]
axes[0, 0].bar(severity_counts.index.astype(str), severity_counts.values, color=colors_sev, edgecolor="white")
axes[0, 0].set_title("Accidents by Severity Level")
axes[0, 0].set_xlabel("Severity (1=Low, 4=High)")
axes[0, 0].set_ylabel("Number of Accidents")
axes[0, 0].grid(axis="y", linestyle="--", alpha=0.5)

hourly = df.groupby("Hour").size()
axes[0, 1].plot(hourly.index, hourly.values, color="#1565C0", linewidth=2.5, marker="o", markersize=4)
axes[0, 1].fill_between(hourly.index, hourly.values, alpha=0.2, color="#1565C0")
axes[0, 1].set_title("Accidents by Hour of Day")
axes[0, 1].set_xlabel("Hour")
axes[0, 1].set_ylabel("Number of Accidents")
axes[0, 1].set_xticks(range(0, 24, 2))
axes[0, 1].grid(linestyle="--", alpha=0.5)

day_counts = df["DayOfWeek"].value_counts().reindex(day_order)
axes[0, 2].bar(day_counts.index, day_counts.values, color="#7E57C2", edgecolor="white")
axes[0, 2].set_title("Accidents by Day of Week")
axes[0, 2].set_ylabel("Number of Accidents")
axes[0, 2].set_xticklabels(day_order, rotation=25, ha="right", fontsize=9)
axes[0, 2].grid(axis="y", linestyle="--", alpha=0.5)

top_states = df["State"].value_counts().head(10)
axes[1, 0].barh(top_states.index[::-1], top_states.values[::-1], color="#26A69A", edgecolor="white")
axes[1, 0].set_title("Top 10 States by Accident Count")
axes[1, 0].set_xlabel("Number of Accidents")
axes[1, 0].grid(axis="x", linestyle="--", alpha=0.5)

top_weather = df["Weather_Condition"].value_counts().head(8)
axes[1, 1].barh(top_weather.index[::-1], top_weather.values[::-1], color="#EF6C00", edgecolor="white")
axes[1, 1].set_title("Top 8 Weather Conditions")
axes[1, 1].set_xlabel("Number of Accidents")
axes[1, 1].grid(axis="x", linestyle="--", alpha=0.5)

day_night = df["Sunrise_Sunset"].value_counts()
axes[1, 2].pie(day_night.values, labels=day_night.index, autopct="%1.1f%%",
               colors=["#FDD835", "#1A237E"], startangle=90,
               wedgeprops={"edgecolor": "white", "linewidth": 1.5})
axes[1, 2].set_title("Day vs Night Accidents")

plt.tight_layout(pad=3.0, h_pad=4.0)
plt.savefig("task04_accident_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("Chart saved as task04_accident_analysis.png")
