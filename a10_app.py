from flask import Flask, request
import os # <-- A 級 Linter 會發現這個 'os' 模組被導入但從未被使用

app = Flask(__name__)

# O 級 SAST 會偵測到這是一個寫死的密鑰
app.config['SECRET_KEY'] = 'my-super-secret-key-do-not-use-in-production'

@app.route("/rolldice")
def roll_dice():
    player = request.args.get('player', default=None, type=str)
    
    # A 級 Linter 會發現下面這行程式碼太長 (超過 79 個字元)
    long_message_for_testing = f"This is an intentionally very long line of code created for the A10 DevSecOps assignment to test if the Flake8 linter correctly identifies lines that exceed the standard PEP 8 character limit."
    
    if player:
        logger.warning(f"{player} is rolling the dice: {result}") # A 級 Linter 會發現 'logger' 和 'result' 未被定義 (NameError)
    else:
        logger.warning(f"Anonymous player is rolling the dice: {result}") # A 級 Linter 會發現 'logger' 和 'result' 未被定義 (NameError)
    
    return "Dice rolled!" # 修正了 A9 的邏輯，使其可以運行

# A 級 Linter 會抱怨函式之間缺少必要的空行
def another_function():

# -----------------------------------------------------------------
# O-LEVEL SAST VULNERABILITY (FOR TRIVY DETECTION)
#
# The key below is a universally recognized example format for an AWS Access Key.
# All SAST scanners (Trivy, Gitleaks, Semgrep) are trained to find this exact pattern.

FAKE_AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE" 

# -----------------------------------------------------------------
