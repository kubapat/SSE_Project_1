import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

tool_paths = {
    "Gradle": "/Users/jakubpataluch/IdeaProjects/EnergiBridge/target/release/gradle.csv",
    "Maven": "/Users/jakubpataluch/IdeaProjects/EnergiBridge/target/release/maven.csv",
    "Bazel": "/Users/jakubpataluch/IdeaProjects/bazel-sample-java/bazel.csv",
}

def main():
    data = {}
    for tool, path in tool_paths.items():
        df = pd.read_csv(path)
        df["Time_s"] = (df["Time"] - df["Time"].iloc[0]) / 1e9
        cpu_cols = [col for col in df.columns if col.startswith("CPU_USAGE_")]
        df["Average_CPU_Usage"] = df[cpu_cols].mean(axis=1)
        df.fillna(0, inplace=True)
        data[tool] = df

    # Plot 1: Average CPU Usage Over Time
    plt.figure(figsize=(10, 5))
    for tool, df in data.items():
        plt.plot(df["Time_s"], df["Average_CPU_Usage"], label=tool)
    plt.xlabel("Time (s)")
    plt.ylabel("Average CPU Usage (%)")
    plt.title("Average CPU Usage Over Time")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("avg_cpu_usage.png")
    plt.show()

    # Plot 2: System Power Over Time
    plt.figure(figsize=(10, 5))
    for tool, df in data.items():
        plt.plot(df["Time_s"], df["SYSTEM_POWER (Watts)"], label=tool)
    plt.xlabel("Time (s)")
    plt.ylabel("System Power (Watts)")
    plt.title("System Power Usage Over Time")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("avg_power.png")
    plt.show()

    # Plot 3: Used Memory Over Time
    plt.figure(figsize=(10, 5))
    for tool, df in data.items():
        plt.plot(df["Time_s"], df["USED_MEMORY"] / (1024**3), label=f"{tool} Memory")
    plt.xlabel("Time (s)")
    plt.ylabel("Memory (GB)")
    plt.title("Used Memory Over Time")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("used_memory.png")
    plt.show()

    # Plot 4: Histogram of System Power
    plt.figure(figsize=(8, 4))
    for tool, df in data.items():
        sns.kdeplot(df["SYSTEM_POWER (Watts)"], label=tool, fill=True, alpha=0.3)
    plt.xlabel("System Power (Watts)")
    plt.title("Distribution of System Power")
    plt.legend()
    plt.tight_layout()
    plt.savefig("power_distribution.png")
    plt.show()

if __name__ == "__main__":
    main()
