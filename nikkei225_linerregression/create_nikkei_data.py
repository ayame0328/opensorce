in_file = input("日経平均株価のcsvを入れる")
out_file = "create_data.csv"

with open(in_file,"rt",encoding="Shift_JIS") as fr:
    lines = fr.readlines()

lines = ["年,月,日,終値,始値,高値,安値\n"]+lines[1:]
lines = map(lambda v: v.replace("/",","),lines)
result_data = "".join(lines).strip()
print(result_data)

with open(out_file,"wt",encoding="utf-8") as fw:
    fw.write(result_data)
    print("save complete.")