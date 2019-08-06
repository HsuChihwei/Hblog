<!--
 * @Author: zhiwei.xu
 * @Date: 2019-08-06 14:34:26
 * @LastEditors: zhiwei.xu
 * @LastEditTime: 2019-08-06 15:18:41
 -->

# git base

# git submodule

## 语法一览

```sh
git submodule [--quiet] [--cached]
git submodule [--quiet] add [<options>] [--] <repository> [<path>]
git submodule [--quiet] status [--cached] [--recursive] [--] [<path>…​]
git submodule [--quiet] init [--] [<path>…​]
git submodule [--quiet] deinit [-f|--force] (--all|[--] <path>…​)
git submodule [--quiet] update [<options>] [--] [<path>…​]
git submodule [--quiet] set-branch [<options>] [--] <path>
git submodule [--quiet] summary [<options>] [--] [<path>…​]
git submodule [--quiet] foreach [--recursive] <command>
git submodule [--quiet] sync [--recursive] [--] [<path>…​]
git submodule [--quiet] absorbgitdirs [--] [<path>…​]
```

## 初始化子模块

```sh
git submodule init
```

## 克隆带子模块的仓库

```sh
git clone project.git project2
cd project2
git submodule init
git submodule update

git clone path.to.project.git project --recursive  # 递归拉取仓库v
```

- 单个克隆子项目，默认不拉取子模块，需要先`init`初始化，再`update`更新子模块

## 创建带子模块的仓库

```sh
cd project
git submodule add path.to.submodule.git submodule

# 以子模块形式给博客新增主题
git submodule add --force https://github.com/Pelican-Elegant/elegant.git themes/elegant
```

- 新增`.gitmodules`文件，里面记载仓库地址与项目路径的映射
- 修改`.git/config`文件，里面会登记子项目的仓库地址及状态

## 更新带子模块的仓库

```sh
git submodule update  # 单个更新
git submodule foreach git pull  # 批量更新
```

## 删除子模块

```sh
git rm --cached submodule_name  # 从git中删除子模块
rm -rf submodule_name/  # 删除子模块目录及源码
vim .gitmodules  # 删除文件中子模块相关代码
vim .git/config  # 删除文件中子模块相关代码
rm .git/module/submodule_name  # 删除目录下子模块对应目录
```

## 查看子模块状态

```sh
git submodule status
```
