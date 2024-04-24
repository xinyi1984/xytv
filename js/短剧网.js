var rule ={
    title: '短剧网',
    host: 'http://5uduanju.com',
    url: '/vodtype/fyclass-fypage.html',
    searchUrl: '/vodsearch/**----------fypage---.html',
    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
    filterable:0,//是否启用分类筛选,
	headers:{//网站的请求头,完整支持所有的,常带ua和cookies
		'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
	},
    class_parse: '.nav&&ul&&li;a&&Text;a&&href;.*/(.*?).html',
    play_parse: true,
    lazy: '',
    limit: 6,
    推荐: '.module-items .module-item;a&&title;img&&data-src;.module-item-text&&Text;a&&href',
    double: true, // 推荐内容是否双层定位
    一级: '.module-items .module-item;a&&title;img&&data-src;.module-item-text&&Text;a&&href',
    二级: {
        "title": "h1&&Text;.module-item-text&&Text",
        "img": ".module-item-pic&&img&&data-src",
        "desc": ".video-info-items:eq(0)&&Text;.video-info-items:eq(1)&&Text;.video-info-items:eq(2)&&Text;",
        "content": ".vod_content&&Text",
        "tabs": ".module-tab-item",
        "lists": ".module-player-list:eq(#id)&&.scroll-content&&a"
        },
        搜索: '.module-items .module-search-item;a&&title;img&&data-src;.video-serial&&Text;a&&href',
        }
