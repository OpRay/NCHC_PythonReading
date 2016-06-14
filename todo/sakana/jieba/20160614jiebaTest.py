# coding=utf-8
import jieba

# jieba.cut 為斷詞, cut_all=True 為全模式, cut_all=False 為精確模式
seg_list = jieba.cut("中文測試", cut_all=True)
print("Full Mode: " + " ".join(seg_list))  # 全模式方式
print("===================")
print()

# jieba.cut 為斷詞, cut_all=True 為全模式, cut_all=False 為精確模式
seg_list = jieba.cut("sakana来到中原大学", cut_all=False)
print("Accurate Mode: " + " ".join(seg_list))  # 精确模式方式
print("===================")
print()

#
seg_list = jieba.cut("他来到了新竹科學園區")  # 預設是精确模式
print("Defaut Mode: " + " ".join(seg_list))
print("===================")
print()

# jieba.cut_for_search 為搜尋引擎模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print("Search Engine Mode: " +", ".join(seg_list))