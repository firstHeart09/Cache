def remove_beginning_simulation_from_file(file_path):
    with open(file_path, 'r') as file:
        log = file.read()
        index = log.find("Beginning simulation!")
        if index != -1:
            log = log[index:]
            return log.split("\n")
        return log.split("\n")

def deal_inst(data):
    # 删除gem5模拟的指令
    out = []
    for line in data:
        if 'Beginning simulation!' in line or '@' not in line or 'Exiting' in line:
            continue
        temp = line.split(':')[4].strip()  # 指令部分mov	MOV_R_I
        # 首先看有没有加号，有的话则判断.在不在+后面的字符串中；没有则判断.在不在字符串中
        temp_1 = line.split(':')[3].strip()  # 0x401abc @get_common_indices.constprop.0+12. 0
        if '+' in temp_1:
            temp_2 = temp_1.split('+')[1]
            if temp.isupper() and '.' in temp_2:
                continue
            else:
                out.append(line)
        else:
            if temp.isupper() and '.' in temp_1:
                continue
            else:
                out.append(line)
    return out

def write(data):
    with open('inst.txt', 'w') as f_out:
        for i in data:
            f_out.write(i + '\n')  # 添加换行符

file_path = "trace.txt"
cleaned_log = remove_beginning_simulation_from_file(file_path)
out = deal_inst(cleaned_log)
write(out)
print(f"Inst count: {len(out)}")
