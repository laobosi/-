import random
import tkinter as tk
from tkinter import scrolledtext, messagebox

def copy_text(text):
    """将文本复制到剪贴板，不显示成功提示"""
    try:
        root.clipboard_clear()
        root.clipboard_append(text)
    except tk.TclError as e:
        messagebox.showerror("错误", f"复制到剪贴板失败: {e}")

def generate_random_text(selected_text_widget, text_data, random_count_var):
    """生成随机文本并显示链接和自定义备注"""
    try:
        # 清空文本区域
        selected_text_widget.delete(1.0, tk.END)
        # 解析输入的随机数
        count = random_count_var.get()
        if count <= 0:
            selected_text_widget.insert(tk.END, "请输入正整数！\n")
            return
        # 解析数据为链接和备注的列表
        text_lines = [line.split(" # ", 1) for line in text_data.strip().split('\n') if line.strip()]
        if not text_lines:
            selected_text_widget.insert(tk.END, "没有可用的数据！\n")
            return
        max_count = min(count, len(text_lines))
        random.shuffle(text_lines)
        # 显示随机选择的链接和备注
        for i in range(max_count):
            link = text_lines[i][0].strip()  # 确保只提取链接
            note = text_lines[i][1].strip() if len(text_lines[i]) > 1 else ""  # 备注可选
            # 创建复制按钮，仅复制链接
            copy_button = tk.Button(
                selected_text_widget,
                text="复制",
                command=lambda t=link: copy_text(t),  # 只传递链接
                cursor="hand2"
            )
            selected_text_widget.window_create(tk.END, window=copy_button)
            # 显示链接和备注（如果有备注）
            display_text = f" {link}"
            if note:
                display_text += f" (备注: {note})"
            selected_text_widget.insert(tk.END, display_text + "\n\n")
    except ValueError:
        selected_text_widget.insert(tk.END, "请输入有效的数字！\n")
    except IndexError:
        selected_text_widget.insert(tk.END, "数据格式错误，请检查输入！\n")

# 主窗口
root = tk.Tk()
root.title("防女巫交互摸奖器")
root.geometry("320x600")  # 减小窗口高度，更加紧凑

# 数据（链接和备注用 # 分隔，未提供备注的链接不显示备注）
text_data_1 = """
https://conft.app/ # 域名，NFT
https://monad.ambient.finance/trade/market/chain
https://swap.bean.exchange/swap
https://www.kuru.io/markets
https://testnet-preview.monorail.xyz/
https://testnet.narwhal.finance/
https://app.uniswap.org/
https://app.crystal.exchange/swap
https://app.hashflow.com/?b=10143-MON&q=10143-WMON
https://testnet.swaps.mace.ag/
https://testnet.rubic.exchange/
https://kintsu.xyz/staking # 质押(kintsu)
https://www.magmastaking.xyz/ # 质押(magma)
https://magiceden.io/monad-testnet # NFT市场(MagicEden)
https://castora.xyz/pools # 预测网站(Castora)
https://www.shmonad.xyz/ # 质押shMonad(Fastlane)
https://testnet.mudigital.net/?utm_source=x&utm_medium=organic&utm_campaign=testnet # (Mudigital mint muBOND)
https://testnet.multipli.fi/ # 质押(Multipli)
https://testnet.nad.fun/ref/aLxqQc # (Nad meme)
https://swmonad.xyz/stake # 质押（swing)
https://glacierfi.com/stake # 质押0.1可以每天领0.5MON
https://app.bhive.finance/#/market/10143/1?action=mint # 借款-还款 质押-解押
https://testnet.morpheus.farm/swap # 交换，加pool池，创建meme币
https://madness.finance/ # 交换，加pool池，质押（质押高奖励）
https://app.kiloex.io/trade # 领USDT下单，然后再Earn存USDT
https://testnet.amertis.exchange/ # Swap
https://mintpad.co/create/edition/ # 部署代币
https://app.monday.trade/ # 用mon换DAK，然后加流动性，然后提取流动性
https://app.bhive.finance/#/market/10143/1?action=mint #借币/还币 质押/解押
"""

text_data_2 = """
https://testnet.somnia.network/swap  # 官方Swap
https://dapp.quickswap.exchange/swap # Quick Swap
https://somnia.exchange/#/swap # 第三方Swap
"""

text_data_3 = """
https://dex.x.ink/ # DEX交互
https://openid.network/name/ # 域名注册
X.ink/XHQYUY # 邀请链接
"""

# 固定链接和密码
official_link_1 = "https://monad.xyz/"
discord_link_1 = "https://discord.gg/monad"
official_link_2 = "https://quest.somnia.network"
discord_link_2 = "https://discord.gg/somnia"
official_link_3 = "https://x.ink/airdrop"
discord_link_3 = "https://discord.com/invite/xosnetwork"
wallet_password = "aa123123"

# “复制钱包密码”按钮
title_frame = tk.Frame(root, padx=2, pady=2)
title_frame.pack(fill="x")
wallet_button = tk.Button(
    title_frame,
    text="复制钱包密码",
    command=lambda: copy_text(wallet_password),
    font=("Arial", 10)
)
wallet_button.pack(anchor="center", pady=1)

# 创建第一个摸奖区域
frame_1 = tk.Frame(root, padx=2, pady=2)
frame_1.pack(fill="both", expand=True)

# 标题和输入数量框横向排列，整体居中
header_frame_1 = tk.Frame(frame_1)
header_frame_1.pack(anchor="center")
random_count_label_1 = tk.Label(header_frame_1, text="Monad随机交互:", font=("Arial", 12))
random_count_label_1.pack(side="left")
random_count_1 = tk.IntVar(value=1)
count_entry_1 = tk.Entry(header_frame_1, textvariable=random_count_1, width=5)
count_entry_1.pack(side="left", padx=5)

# 随机选择、官方或生态、Discord 按钮横向排列
button_frame_1 = tk.Frame(frame_1)
button_frame_1.pack(anchor="center")
generate_button_1 = tk.Button(
    button_frame_1,
    text="随机选择",
    command=lambda: generate_random_text(selected_text_1, text_data_1, random_count_1),
    font=("Arial", 10)
)
generate_button_1.pack(side="left", padx=5)
official_button_1 = tk.Button(
    button_frame_1,
    text="官方或生态",
    command=lambda: copy_text(official_link_1),
    font=("Arial", 10)
)
official_button_1.pack(side="left", padx=5)
discord_button_1 = tk.Button(
    button_frame_1,
    text="Discord",
    command=lambda: copy_text(discord_link_1),
    font=("Arial", 10)
)
discord_button_1.pack(side="left", padx=5)

selected_text_1 = scrolledtext.ScrolledText(
    frame_1, height=2, width=30, wrap=tk.WORD, font=("Arial", 10), borderwidth=1, relief="solid"
)
selected_text_1.pack(fill="both", expand=True)

# 创建第二个摸奖区域
frame_2 = tk.Frame(root, padx=2, pady=2)
frame_2.pack(fill="both", expand=True)

# 标题和输入数量框横向排列，整体居中
header_frame_2 = tk.Frame(frame_2)
header_frame_2.pack(anchor="center")
random_count_label_2 = tk.Label(header_frame_2, text="Somnia项目:", font=("Arial", 12))
random_count_label_2.pack(side="left")
random_count_2 = tk.IntVar(value=1)
count_entry_2 = tk.Entry(header_frame_2, textvariable=random_count_2, width=5)
count_entry_2.pack(side="left", padx=5)

# 随机选择、奥德赛和每日签到、Discord 按钮横向排列
button_frame_2 = tk.Frame(frame_2)
button_frame_2.pack(anchor="center")
generate_button_2 = tk.Button(
    button_frame_2,
    text="随机选择",
    command=lambda: generate_random_text(selected_text_2, text_data_2, random_count_2),
    font=("Arial", 10)
)
generate_button_2.pack(side="left", padx=5)
official_button_2 = tk.Button(
    button_frame_2,
    text="奥德赛和每日签到",
    command=lambda: copy_text(official_link_2),
    font=("Arial", 10)
)
official_button_2.pack(side="left", padx=5)
discord_button_2 = tk.Button(
    button_frame_2,
    text="Discord",
    command=lambda: copy_text(discord_link_2),
    font=("Arial", 10)
)
discord_button_2.pack(side="left", padx=5)

selected_text_2 = scrolledtext.ScrolledText(
    frame_2, height=2, width=30, wrap=tk.WORD, font=("Arial", 10), borderwidth=1, relief="solid"
)
selected_text_2.pack(fill="both", expand=True)

# 创建第三个摸奖区域
frame_3 = tk.Frame(root, padx=2, pady=2)
frame_3.pack(fill="both", expand=True)

# 标题和输入数量框横向排列，整体居中
header_frame_3 = tk.Frame(frame_3)
header_frame_3.pack(anchor="center")
random_count_label_3 = tk.Label(header_frame_3, text="XOS项目:", font=("Arial", 12))
random_count_label_3.pack(side="left")
random_count_3 = tk.IntVar(value=1)
count_entry_3 = tk.Entry(header_frame_3, textvariable=random_count_3, width=5)
count_entry_3.pack(side="left", padx=5)

# 随机选择、每日签到、Discord 按钮横向排列
button_frame_3 = tk.Frame(frame_3)
button_frame_3.pack(anchor="center")
generate_button_3 = tk.Button(
    button_frame_3,
    text="随机选择",
    command=lambda: generate_random_text(selected_text_3, text_data_3, random_count_3),
    font=("Arial", 10)
)
generate_button_3.pack(side="left", padx=5)
official_button_3 = tk.Button(
    button_frame_3,
    text="每日签到",
    command=lambda: copy_text(official_link_3),
    font=("Arial", 10)
)
official_button_3.pack(side="left", padx=5)
discord_button_3 = tk.Button(
    button_frame_3,
    text="Discord",
    command=lambda: copy_text(discord_link_3),
    font=("Arial", 10)
)
discord_button_3.pack(side="left", padx=5)

selected_text_3 = scrolledtext.ScrolledText(
    frame_3, height=2, width=30, wrap=tk.WORD, font=("Arial", 10), borderwidth=1, relief="solid"
)
selected_text_3.pack(fill="both", expand=True)

root.mainloop()