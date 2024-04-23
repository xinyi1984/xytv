var rule ={
    title: '短剧网',
    host: 'http://www.duanjutv.cc',
    url: '/vodtype/fyclass-fypage.html',
    searchUrl: '/vodsearch/**----------fypage---.html',
    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
    filterable:0,//是否启用分类筛选,
    class_parse: '.stui-header__menu&&li;a&&Text;a&&href;.*/(.*?).html',
    play_parse: true,
    lazy: '',
    limit: 6,
     推荐: '.stui-pannel_bd;ul&&li;a&&title;img&&src;a&&href',
    double: true, // 推荐内容是否双层定位
    一级: '.stui-pannel_bd;ul&&li;a&&title;img&&src;a&&href',
    二级: {
        "title": ".title&&Text;.detail-sketch&&Text",
        "img": ".img&&img&&src",
        "desc": ".stui-content__detail&&p:eq(1)&&Text.stui-content__detail&&p:eq(1)&&Text;.stui-content__detail&&p:eq(2)&&Text;.stui-content__detail&&p:eq(3)&&Text",
        "content": ".detail-sketch&&Text",
        "tabs": ".title&&Text",
        "lists": ".stui-content__playlist:eq(#id)&&li"
        },
        搜索: '.module-items .module-search-item;a&&title;img&&data-src;.video-serial&&Text;a&&href',
        }
