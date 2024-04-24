var rule ={
    title: '短剧网',
    host: 'http://www.duanjutv.cc',
    url: '/vodtype/fyclass-fypage.html',
    searchUrl: '/vodsearch/-------------.html?wd=**',
    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
    filterable:0,//是否启用分类筛选,
    headers: {'User-Agent@Mozilla/5.0 (Linux; Android 11; Mi 10 Pro) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36'},
    class_parse: '.stui-header__menu li;a&&Text;a&&href;.*/(.*?).html',
    play_parse: true,
    lazy: '',
    limit: 6,
    推荐: '.stui-pannel_bd;ul&&li;a&&title;img&&src;a&&href',
    double: true, // 推荐内容是否双层定位
    一级: '.stui-pannel_bd .stui-vodlist__box;a&&title;img&&src;.pic-text&&Text;a&&href',
    二级: {
        "title": "h3&&Text;p:eq(0)&&Text",
        "img": "img&&src",
        "desc": "p:eq(1)&&Text;p:eq(2)&&Text;p:eq(3)&&Text",
        "content": "p:eq(4)&&Text",
        "tabs": ".stui-pannel__head&&.title&&Text",
        "lists": ".stui-content__playlist:eq(#id) li"
        },
        搜索: '.module-items .module-search-item;a&&title;img&&data-src;.video-serial&&Text;a&&href',
        }
