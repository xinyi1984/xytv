var rule = {
    title: '短剧tv',
    host: 'http://www.duanjutv.cc/',
    searchUrl: '/vodsearch/**----------fypage---.html',
    url:'/vodtype/fyclass-fypage',
    searchable:2,
    quickSearch:1,
    filterable:0,
    headers: {
                'User-Agent@Mozilla/5.0 (Linux；； Android 11；； Mi 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36'
            },
    timeout: 5000,
    class_parse: '.stui-header__menu&&li;a&&title;a&&href;.*/(.*?).html',
    cate_exclude: '明星|专题|最新|排行',
    limit: 40,
    play_parse: true,
    lazy: '',
    推荐: '.stui-pannel_bd;ul&&li;a&&title;img&&src;a&&href',
    double: true,
    一级: '.stui-pannel_bd;ul&&li;a&&title;img&&src;a&&href',
    二级: {
        "title": ".title&&Text;.detail-sketch&&Text",
        "img": ".img&&img&&src",
        "desc": ".stui-content__detail&&p:eq(1)&&Text.stui-content__detail&&p:eq(1)&&Text;.stui-content__detail&&p:eq(2)&&Text;.stui-content__detail&&p:eq(3)&&Text",
        "content": ".detail-sketch&&Text",
        "tabs": ".title&&Text",
        "lists": ".stui-content__playlist:eq(#id)&&li"
        },
    搜索: '.hl-list-item;a&&title;a&&data-original;.remarks&&Text;a&&href',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 0,//是否启用分类筛选,
        }
