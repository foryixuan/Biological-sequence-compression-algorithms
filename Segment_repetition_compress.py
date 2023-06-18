from collections import Counter
import matplotlib.pyplot as plt

class SequenceCompressor:
    def __init__(self, input_sequence):
        self.input_sequence = input_sequence
        self.codetable_list = []  # 存储不同N值下的压缩结果
        self.compression_ratios = []  # 存储压缩率
        self.sequence_lengths = []  # 存储压缩后的序列长度

    def substitute(self, input_sequence, codetable):
        # 将压缩后的序列中的段替换为对应的字符
        for index, segment in codetable.items():
            input_sequence = input_sequence.replace(segment, chr(index + 33))
        
        return input_sequence

    def compress(self):
        for n in range(5, 11):  # 遍历不同的N值
            codetable = {}  # 存储每个N值下的编码表
            temp_sequence = self.input_sequence  # 临时存储当前序列，用于迭代压缩
            
            processed_segments = set()  # 存储已处理过的段，避免重复处理
            
            while True:
                # 统计当前序列中各个长度为N的段的频率
                frequencies = Counter([temp_sequence[i:i+n] for i in range(len(temp_sequence)-n+1)])
                most_common_segment = max(frequencies, key=frequencies.get)  # 找到出现次数最多的段
                
                # 如果出现次数最多的段的频率小于等于1或者该段已经被处理过，则结束循环
                if frequencies[most_common_segment] <= 1 or most_common_segment in processed_segments:
                    break
                
                # 将出现次数最多的段添加到编码表中，并用对应的字符替换序列中的该段
                codetable[len(codetable)+1] = most_common_segment
                temp_sequence = temp_sequence.replace(most_common_segment, chr(len(codetable) + 32))
                processed_segments.add(most_common_segment)
            
            self.codetable_list.append((codetable, temp_sequence))

    def print_compression_results(self):
        for i, (codetable, compressed_sequence) in enumerate(self.codetable_list):
            print("N =", i+5)  # 输出当前的N值
            print("Codetable:")
            total_storage = 0
            for index, segment in codetable.items():
                storage = len(segment) * 8  # 计算该段的存储位数
                total_storage += storage
                print(f"{chr(index + 32)}: {segment} (Storage: {storage} bits)")
            print("Compressed sequence:", self.substitute(compressed_sequence, codetable))  # 输出压缩后的序列
            print("Length:", len(compressed_sequence))  # 输出压缩后序列的长度
            
            original_storage = len(self.input_sequence) * 8  # 原始序列的存储位数
            codetable_storage = total_storage  # 编码表的存储位数
            total_storage = len(compressed_sequence) * 8 + codetable_storage  # 总的存储位数
            compression_ratio = (total_storage / original_storage) * 100  # 计算压缩率
            print("Original Sequence Storage:", original_storage, "bits")
            print("Codetable Storage:", codetable_storage, "bits")
            print("Total Storage:", total_storage, "bits")
            print("Compression Ratio: %.2f%%" % compression_ratio)
            print("--------------------------")

    def calculate_compression_ratio(self):
        for codetable, compressed_sequence in self.codetable_list:
            original_storage = len(self.input_sequence) * 8  # 原始序列的存储位数
            codetable_storage = sum(len(segment) * 8 for segment in codetable.values())  # 编码表的存储位数
            total_storage = len(compressed_sequence) * 8 + codetable_storage  # 总的存储位数
            compression_ratio = (total_storage / original_storage) * 100  # 计算压缩率
            self.compression_ratios.append(compression_ratio)

    def calculate_sequence_length(self):
        for _, compressed_sequence in self.codetable_list:
            self.sequence_lengths.append(len(compressed_sequence))

# 创建压缩器对象并进行压缩
input_sequence = "TGACTGACTAGACTGACTGACTGACTGACTGACTCTCTATACACTATGACTGACTGACTGCTATACGACTGACTGACTGACTGACTACGACTGACTCTAAAAGACTGACTATGACTGACTGACTGACTACGACTGACTGACTGACTGACTGACTGACTGACTGACTGGGCTAGACTACTGCATCTAGTAACT"
compressor = SequenceCompressor(input_sequence)
compressor.compress()
compressor.calculate_compression_ratio()
compressor.calculate_sequence_length()

# 获取N值、压缩率和压缩后序列长度数据
N_values = [5, 6, 7, 8, 9, 10]
compression_ratios = compressor.compression_ratios
sequence_lengths = compressor.sequence_lengths

# 创建画布和两个子图
fig, ax1 = plt.subplots()

# 绘制压缩率折线图
ax1.plot(N_values, compression_ratios, 'b-')
ax1.set_xlabel('N')
ax1.set_ylabel('Compression Ratio (%)', color='b')
ax1.tick_params('y', colors='b')

# 创建第二个纵坐标轴，并绘制压缩后序列长度折线图
ax2 = ax1.twinx()
ax2.plot(N_values, sequence_lengths, 'r-')
ax2.set_ylabel('Compressed Sequence Length', color='r')
ax2.tick_params('y', colors='r')

# 添加图例
ax1.legend(['Compression Ratio'], loc='upper left')
ax2.legend(['Sequence Length'], loc='upper right')

# 设置标题
plt.title('Compression Ratio and Sequence Length vs N')

# 展示图表
plt.show()

# 打印压缩结果
compressor.print_compression_results()

