import csv
import pandas as pd


def read_csv(filename):
    csv_data = []
    csv_path = filename
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    return csv_data


def read_excel():
    excel_path = "excels/MHPP Analysis.xlsx"
    df = pd.read_excel(excel_path, sheet_name="MHPP_benchmark_final_plan")
    data = [
        {"model": x,
         "total_greedy": f"{y * 100:.1f}%",
         "link": z,
         "distraction_greedy": f"{distraction_greedy * 100:.1f}%",
         "redefination_greedy":  f"{redefination_greedy * 100:.1f}%",
         "shortcut_greedy": f"{shortcut_greedy * 100:.1f}%",
         "commonsense_greedy": f"{commonsense_greedy * 100:.1f}%",
         "cornercase_greedy": f"{cornercase_greedy * 100:.1f}%",
         "complex_greedy": f"{complex_greedy * 100:.1f}%",
         "codesense_greedy": f"{codesense_greedy * 100:.1f}%",
         } for x, y, z, distraction_greedy, redefination_greedy, shortcut_greedy,
        commonsense_greedy, cornercase_greedy, complex_greedy, codesense_greedy in zip(
            df.iloc[:, 1].tolist(), df.iloc[:, 10].tolist(), df.iloc[:,11].tolist(),
            df.iloc[:, 3].tolist(), df.iloc[:, 4].tolist(), df.iloc[:, 5].tolist(),
            df.iloc[:, 6].tolist(), df.iloc[:, 7].tolist(), df.iloc[:, 8].tolist(),
            df.iloc[:, 9].tolist(),
        )
    ]
    new_data = []
    for line in data[:33]:
        if not line["total_greedy"] or line["total_greedy"] == "nan%":
            continue
        new_data.append(line)
    return new_data


def manual_data_greedy():
    # total, distraction, redefination, shortcut, commonsense, cornercase, complex, codesense
    greedy_data = {
        "Llama2 Chat 7b": ["2.9%", "0.0%", "0.0%", "0.0%", "5.0%", "10.0%", "0.0%", "10.0%"],
        "Llama2 Chat 13b": ["2.1%", "0.0%", "0.0%", "0.0%", "0.0%", "10.0%", "0.0%", "5.0%"],
        "Mistral 7b": ["7.9%", "15.0%", "0.0%", "0.0%", "25.0%", "0.0%", "15.0%", "0.0%"],
        "Phi 1": ["12.9%", "10.0%", "15.0%", "10.0%", "10.0%", "10.0%", "5.0%", "30.0%"],
        "Phi 1.5": ["8.6%", "0.0%", "10.0%", "5.0%", "15.0%", "10.0%", "0.0%", "20.0%"],
        "Phi 2": ["13.6%", "10.0%", "15.0%", "15.0%", "25.0%", "10.0%", "0.0%", "20.0%"],
        "CodeLlama 7B": ["3.6%", "0.0%", "0.0%", "0.0%", "10.0%", "10.0%", "0.0%", "5.0%"],
        "CodeLlama 13B": ["5.0%", "0.0%", "5.0%", "0.0%", "10.0%", "10.0%", "0.0%", "10.0%"],
        "CodeLlama 7B Instruct": ["8.6%", "5.0%", "5.0%", "5.0%", "15.0%", "15.0%", "0.0%", "15.0%"],
        "CodeLlama 13B Instruct": ["15.0%", "20.0%", "15.0%", "10.0%", "15.0%", "15.0%", "10.0%", "20.0%"],
        "CodeLlama 34B Instruct": ["16.4%", "20.0%", "25.0%", "10.0%", "25.0%", "5.0%", "5.0%", "25.0%"],
        "CodeLlama 7B Py": ["3.6%", "0.0%", "5.0%", "0.0%", "10.0%", "5.0%", "0.0%", "5.0%"],
        "CodeLlama 13B Py": ["5.0%", "0.0%", "5.0%", "0.0%", "10.0%", "10.0%", "0.0%", "10.0%"],
        "CodeLlama 34B Py": ["9.3%", "10.0%", "10.0%", "0.0%", "25.0%", "10.0%", "5.0%", "5.0%"],
        "DeepSeek Instruct 1.3B": ["11.4%", "5.0%", "10.0%", "5.0%", "30.0%", "20.0%", "0.0%", "10.0%"],
        "DeepSeek Instruct 6.7B": ["22.9%", "15.0%", "35.0%", "10.0%", "30.0%", "20.0%", "10.0%", "40.0%"],
        "DeepSeek Instruct 33B": ["38.6%", "30.0%", "40.0%", "20.0%", "60.0%", "45.0%", "30.0%", "45.0%"],
        "WizardCoder-33B-V1.1": ["31.4%", "20.0%", "30.0%", "15.0%", "65.0%", "35.0%", "15.0%", "40.0%"],
        "WizardCoder-Python-34B-V1.0": ["22.9%", "15.0%", "35.0%", "10.0%", "40.0%", "15.0%", "10.0%", "35.0%"],
        "GPT-3.5 (gpt-3.5-turbo)": ["27.9%", "25.0%", "40.0%", "25.0%", "30.0%", "15.0%", "15.0%", "45.0%"],
        "GPT-4 (gpt-4-1106-preview)": ["53.6%", "35.0%", "65.0%", "40.0%", "70.0%", "55.0%", "55.0%", "55.0%"]
    }
    return greedy_data

def manual_data_sampling():
    # c1 p1, c1 p5, c2 p1, c2 p5, c3 p1, c3 p5, c4 p1, c4 p5, c5 p1, c5 p5, c6 p1, c6 p5, c7 p1, c7 p5, tot p1, tot p5, prompted
    sampling_data = {
        "DeepSeek-Coder-V2-0724": ["35.2%", "44.9%", "53.3%", "65.1%", "37.3%", "45.6%", "72.2%", "75.7%",
                                   "50.8%", "53.9%", "40.1%", "56.2%", "55.6%", "62.8%", "49.2%", "57.7%", "TRUE"],
        "GPT-4o mini": ["47.6%", "57.0%", "59.7%", "74.9%", "41.2%", "60.1%", "58.3%", "70.9%", "46.5%", "59.3%",
                        "35.5%", "48.4%", "54.5%", "67.0%", "49.0%", "62.5%", "TRUE"],
    }

    return sampling_data

def save_csv(path, data):
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    print("{} saved".format(path))


def main():
    greedy_data = manual_data_greedy()
    sampling_data = manual_data_sampling()
    csv_data = read_csv("mhpp.csv")
    for idx, line in enumerate(csv_data):
        if idx == 0:
            line += ["Greedy", "Greedy distraction", "Greedy redefination", "Greedy shortcut", "Greedy commonsense", "Greedy cornercase", "Greedy complex", "Greedy codesense"]
            # line.append("Greedy")
        else:
            line += greedy_data[line[0]]
            # line.append(greedy_data[line[0]])

    excel_data = read_excel()
    for line in excel_data:
        if line["model"] in sampling_data.keys():
            sampling_part = sampling_data[line["model"]]
        else:
            sampling_part = ["-"] * 17
        new_line = ([line["model"]] + sampling_part +
                    [line["link"], line["total_greedy"], line["distraction_greedy"],
                     line["redefination_greedy"], line["shortcut_greedy"], line["commonsense_greedy"],
                     line["cornercase_greedy"], line["complex_greedy"], line["codesense_greedy"],
                     ])
        csv_data.append(new_line)
    title_line = sorted(csv_data[0])
    output_csv = "140_mhpp.csv"
    save_csv(output_csv, csv_data)
    return title_line


def new_main():
    excel_path = "excels/MHPP_ICLR.xlsx"
    df = pd.read_excel(excel_path, sheet_name="MHPP_leaderboard")
    csv_data = [df.columns.tolist()] + df.values.tolist()
    title_line = sorted(csv_data[0])
    output_csv = "new_mhpp.csv"
    save_csv(output_csv, csv_data)
    return title_line


if __name__ == '__main__':
    old_title_line = main()
    new_title_line = new_main()
    diff = set(old_title_line) - set(new_title_line)
    print(diff)
    assert old_title_line == new_title_line
