<!--
 * @Author: zhiwei.xu
 * @Date: 2019-08-06 14:09:42
 * @LastEditors: zhiwei.xu
 * @LastEditTime: 2019-08-06 14:20:15
 -->

# snippets

## gen ssh

```sh
ssh-keygen -t rsa -b 4096 -C "zhiwei.xu@mac"
cd /Users/chihwei-hsu/.ssh/  # 进入key生成位置
vim id_rsa  # 私钥
vim id_rsa.pub  # 公钥
vim authorized_keys  # 公钥加入，免密登录  
```
