var rule = {
    title: '迷迷剧',
    host: 'https://mimiju.com',
    searchUrl: '/v_search/**----------fypage---.html',
    url:'/vodshow/fyclass--------fypage---.html',
    filterable:1,//是否启用分类筛选,
    filter_url:'fypage---{{fl.ZM}}---{{fl.by}}',
    filter:{
        "20":[{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
        "22":[{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
        "21":[{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
        "24":[{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}],
        "23":[{"key":"by","name":"排序","value":[{"n":"时间","v":"time"},{"n":"人气","v":"hits"},{"n":"评分","v":"score"}]}]
    },
    filter_def:{
        20:{cateId:'20'},
        22:{cateId:'22'},
        21:{cateId:'21'},
        24:{cateId:'24'},
        23:{cateId:'23'}
    },
            class_parse: 'body&&.hl-nav li:gt(0);a&&Text;a&&href;.*/(.*?).html',
            cate_exclude: '明星|专题|最新|排行',
            limit: 40,
            play_parse: true,
            lazy: '',
            推荐: '.hl-vod-list;li;a&&title;a&&data-original;.remarks&&Text;a&&href',
            double: true,
            一级: '.hl-vod-list&&.hl-list-item;a&&title;a&&data-original;.remarks&&Text;a&&href',
            二级: {
                "title": ".hl-infos-title&&Text;.hl-text-conch&&Text",
                "img": ".hl-lazy&&data-original",
                "desc": ".hl-infos-content&&.hl-text-conch&&Text",
                "content": ".hl-content-text&&Text",
                "tabs": ".hl-tabs&&a",
                "lists": ".hl-plays-list:eq(#id)&&li"
            },
            搜索: '.hl-list-item;a&&title;a&&data-original;.remarks&&Text;a&&href',
            searchable: 2,//是否启用全局搜索,
            quickSearch: 0,//是否启用快速搜索,
            filterable: 0,//是否启用分类筛选,
        }
