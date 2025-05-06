import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    df = pd.read_csv("/Users/jakubpataluch/IdeaProjects/EnergiBridge/target/release/maven.csv")
    df["Time_s"] = (df["Time"] - df["Time"].iloc[0]) / 1e9
    df.fillna(0, inplace=True) # Filling NaNs

    # Plot 1: CPU Usage per core
    cpu_usage_cols = [col for col in df.columns if col.startswith("CPU_USAGE_")]
    df["Average_CPU_Usage"] = df[cpu_usage_cols].mean(axis=1)

    plt.figure(figsize=(12, 6))
    for col in cpu_usage_cols:
        plt.plot(df["Time_s"], df[col], alpha=0.5, label=col)
    plt.plot(df["Time_s"], df["Average_CPU_Usage"], color='black', linewidth=2, label="Average CPU Usage")
    plt.xlabel("Time (s)")
    plt.ylabel("CPU Usage (%)")
    plt.title("CPU Usage per Core Over Time")
    plt.legend(loc="upper right", ncol=4)
    plt.tight_layout()
    plt.grid()
    plt.savefig("cpu_usage_per_core.png")
    plt.show()

    # Plot 2: System Power Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df["Time_s"], df["SYSTEM_POWER (Watts)"], color='green')
    plt.xlabel("Time (s)")
    plt.ylabel("Power (Watts)")
    plt.title("System Power Usage Over Time")
    plt.grid()
    plt.tight_layout()
    plt.savefig("system_power.png")
    plt.show()

    #Plot 3: Used Memory Over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df["Time_s"], df["USED_MEMORY"] / (1024**3), label="Used Memory (GB)")
    plt.plot(df["Time_s"], df["USED_SWAP"] / (1024**3), label="Used Swap (GB)", linestyle='--')
    plt.xlabel("Time (s)")
    plt.ylabel("Memory (GB)")
    plt.title("Memory and Swap Usage Over Time")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("memory_usage.png")
    plt.show()

    #Plot 4: Histogram of Power Usage
    plt.figure(figsize=(8, 4))
    sns.histplot(df["SYSTEM_POWER (Watts)"], bins=30, kde=True, color="orange")
    plt.xlabel("System Power (Watts)")
    plt.title("Distribution of System Power")
    plt.tight_layout()
    plt.savefig("power_histogram.png")
    plt.show()

if __name__ == "__main__":
    main()