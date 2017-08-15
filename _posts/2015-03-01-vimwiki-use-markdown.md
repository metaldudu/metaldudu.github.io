---
layout: post
title: "Vimwiki支持markdown"
description: ""
category: geek
tags: []
---


## 安装步骤

1. 确保Vim正常，你的vimrc要包含以下部分：

        set nocompatible 
        filetype plugin on 
        syntax on

2. 下载vimwiki，主页地址：http://www.vim.org/scripts/script.php?script_id=2226
3. 用Vim打开下载到的vimwiki-x-x.vba，执行安装命令：`:so %`

## 使用

1. 使用<leader>ww 打开wiki，通常是输入“\ww”。
2. 第一次会提醒你wiki的位置，你可以先生成一份配置信息，稍后再编辑vimrc。
3. 参考别人的配置，比如：http://my.oschina.net/u/250670/blog/79241
4. 如何编辑wiki，也参考Vimwiki主页
5. 输出HTML： `Vimwiki2HTML` 命令转换当前页，`VimwikiAll2HTML` 命令转换全部。

## markdown支持

Vimwiki已经支持markdown，但目前版本不支持直接导出html。所以必须用第三方脚本来转换。方案如下：

1. 配置支持markdown，可以参考：http://www.zhihu.com/question/20207987

2. 配置脚本，下载 [misaka_md2html.py](https://github.com/tub78/misaka-bootstrap/blob/master/bin/misaka_md2html.py)并按照文件内说明配置
  * 安装：misaka Jinja2，可能需要python3支持
  * 确保可执行：`chmod 755 misaka_md2html.py`
  * 修改 vimrc 的配置，使 custom_wiki2html 指向此文件
  * 设置 path_html ，也就是输出目录
  * 设置 syntax ，等于 markdown
  * 拷贝一份 style.css 放到 path_html，比如vimwiki内置的css：vim/autoload/vimwiki/style.css
3. 以下是我的配置：

        let g:vimwiki_list = [
        \{"path": "~/myblog/vimwiki/", 
        \ "path_html": "~/myblog/wiki/",
        \ "syntax": "markdown", 
        \ "ext": ".md",
        \ "css_file": '~/myblog/vimwiki/wiki/style.css',
        \ "custom_wiki2html": "~/myblog/vimwiki/misaka_md2html.py",
        \ "auto_export": 0}
        \]

4. 修改此脚本的错误，**注意**：按照下面参考文章的解释，需要修改misaka_md2html.py，添加4个参数。即：

        parser.add_argument("cssfile", help="The css file (with absolute path) to "
            "be referenced in the resulting html file.")
        # modification start here_
        parser.add_argument("template_path", help="The css file (with absolute path) to "
            "be referenced in the resulting html file.")
        parser.add_argument("template_default", help="The css file (with absolute path) to "
            "be referenced in the resulting html file.")
        parser.add_argument("template_ext", help="The css file (with absolute path) to "
            "be referenced in the resulting html file.")
        parser.add_argument("root_path", help="The css file (with absolute path) to "
            "be referenced in the resulting html file.")
        # modification ends
        ns = parser.parse_args()
    
#### 参考：

+ http://weblog.donie.me/2014/06/01/vimwiki_markdown.html


## 修正css绝对路径

用上面的脚本转换，生成的html中包含css绝对路径，批量修改命令：

    sed -i "s#/where/your/wiki/style.css#style.css#g" `grep style.css -rl /where/your/wiki`


##其他

暂时可以正常使用了，每一个wiki页面都是单独的markdown文件，可以自由组织和转换，并且可以快速发布到网站上。比如我的[wiki页面](http://metaldudu.github.io/wiki/index.html)。

`20140301`

