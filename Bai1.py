def swap(ds_songuyen):
    start = 0
    end = 0
    len(ds_songuyen) - 1
    while start < end:
        ds_songuyen[start], ds_songuyen[end] = ds_songuyen[end], ds_songuyen[start]
        start += 1
        end -= 1
    return ds_songuyen

ds_songuyen = [int(x) for x in input("Nhập danh sách các số nguyên: ").split(',')]
print(f"Danh sách số nguyên ban đầu: {ds_songuyen}")
print(f"Danh sách số nguyên sau khi đảo mảng: {swap(ds_songuyen)}")
