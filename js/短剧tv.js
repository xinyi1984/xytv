var rule ={
    title: '短剧网',
    host: 'http://www.duanjutv.cc',
    url: '/vodtype/fyclass-fypage.html',
    searchUrl: '/vodsearch/-------------.html?wd=**&submit=',
    searchable: 2,//是否启用全局搜索,
    quickSearch: 0,//是否启用快速搜索,
    filterable:0,//是否启用分类筛选,
    filter_url:'--{{fl.by}}---{{fl.letter}}---fypage---',
    filter:{
        "nixi":[{"key":"letter","name":"字母","value":[{"n":"A","v":"A"},{"n":"B","v":"B"},{"n":"C","v":"C"},{"n":"D","v":"D"},{"n":"E","v":"E"},{"n":"F","v":"F"},{"n":"G","v":"G"},{"n":"H","v":"H"},{"n":"I","v":"I"},{"n":"J","v":"J"},{"n":"K","v":"K"},{"n":"L","v":"L"},{"n":"M","v":"M"},{"n":"N","v":"N"},{"n":"O","v":"O"},{"n":"P","v":"P"},{"n":"Q","v":"Q"},{"n":"R","v":"R"},{"n":"S","v":"S"},{"n":"T","v":"T"},{"n":"U","v":"U"},{"n":"V","v":"V"},{"n":"W","v":"W"},{"n":"X","v":"X"},{"n":"Y","v":"Y"},{"n":"Z","v":"Z"},{"n":"0-9","v":"0-9"}]},
                  {"key":"by","name":"排序","value":[{"n":"时间排序","v":"time"},{"n":"人气排序","v":"hits"},{"n":"评分排序","v":"score"}]}],
        "tianchong":[{"key":"letter","name":"字母","value":[{"n":"A","v":"A"},{"n":"B","v":"B"},{"n":"C","v":"C"},{"n":"D","v":"D"},{"n":"E","v":"E"},{"n":"F","v":"F"},{"n":"G","v":"G"},{"n":"H","v":"H"},{"n":"I","v":"I"},{"n":"J","v":"J"},{"n":"K","v":"K"},{"n":"L","v":"L"},{"n":"M","v":"M"},{"n":"N","v":"N"},{"n":"O","v":"O"},{"n":"P","v":"P"},{"n":"Q","v":"Q"},{"n":"R","v":"R"},{"n":"S","v":"S"},{"n":"T","v":"T"},{"n":"U","v":"U"},{"n":"V","v":"V"},{"n":"W","v":"W"},{"n":"X","v":"X"},{"n":"Y","v":"Y"},{"n":"Z","v":"Z"},{"n":"0-9","v":"0-9"}]},
                    {"key":"by","name":"排序","value":[{"n":"时间排序","v":"time"},{"n":"人气排序","v":"hits"},{"n":"评分排序","v":"score"}]}],
        "nuelian":[{"key":"letter","name":"字母","value":[{"n":"A","v":"A"},{"n":"B","v":"B"},{"n":"C","v":"C"},{"n":"D","v":"D"},{"n":"E","v":"E"},{"n":"F","v":"F"},{"n":"G","v":"G"},{"n":"H","v":"H"},{"n":"I","v":"I"},{"n":"J","v":"J"},{"n":"K","v":"K"},{"n":"L","v":"L"},{"n":"M","v":"M"},{"n":"N","v":"N"},{"n":"O","v":"O"},{"n":"P","v":"P"},{"n":"Q","v":"Q"},{"n":"R","v":"R"},{"n":"S","v":"S"},{"n":"T","v":"T"},{"n":"U","v":"U"},{"n":"V","v":"V"},{"n":"W","v":"W"},{"n":"X","v":"X"},{"n":"Y","v":"Y"},{"n":"Z","v":"Z"},{"n":"0-9","v":"0-9"}]},
                     {"key":"by","name":"排序","value":[{"n":"时间排序","v":"time"},{"n":"人气排序","v":"hits"},{"n":"评分排序","v":"score"}]}],
        "chuanyue":[{"key":"letter","name":"字母","value":[{"n":"A","v":"A"},{"n":"B","v":"B"},{"n":"C","v":"C"},{"n":"D","v":"D"},{"n":"E","v":"E"},{"n":"F","v":"F"},{"n":"G","v":"G"},{"n":"H","v":"H"},{"n":"I","v":"I"},{"n":"J","v":"J"},{"n":"K","v":"K"},{"n":"L","v":"L"},{"n":"M","v":"M"},{"n":"N","v":"N"},{"n":"O","v":"O"},{"n":"P","v":"P"},{"n":"Q","v":"Q"},{"n":"R","v":"R"},{"n":"S","v":"S"},{"n":"T","v":"T"},{"n":"U","v":"U"},{"n":"V","v":"V"},{"n":"W","v":"W"},{"n":"X","v":"X"},{"n":"Y","v":"Y"},{"n":"Z","v":"Z"},{"n":"0-9","v":"0-9"}]},
                  {"key":"by","name":"排序","value":[{"n":"时间排序","v":"time"},{"n":"人气排序","v":"hits"},{"n":"评分排序","v":"score"}]}],
        "chongsheng":[{"key":"letter","name":"字母","value":[{"n":"A","v":"A"},{"n":"B","v":"B"},{"n":"C","v":"C"},{"n":"D","v":"D"},{"n":"E","v":"E"},{"n":"F","v":"F"},{"n":"G","v":"G"},{"n":"H","v":"H"},{"n":"I","v":"I"},{"n":"J","v":"J"},{"n":"K","v":"K"},{"n":"L","v":"L"},{"n":"M","v":"M"},{"n":"N","v":"N"},{"n":"O","v":"O"},{"n":"P","v":"P"},{"n":"Q","v":"Q"},{"n":"R","v":"R"},{"n":"S","v":"S"},{"n":"T","v":"T"},{"n":"U","v":"U"},{"n":"V","v":"V"},{"n":"W","v":"W"},{"n":"X","v":"X"},{"n":"Y","v":"Y"},{"n":"Z","v":"Z"},{"n":"0-9","v":"0-9"}]},
                   {"key":"by","name":"排序","value":[{"n":"时间排序","v":"time"},{"n":"人气排序","v":"hits"},{"n":"评分排序","v":"score"}]}]
    },
    class_name:'逆袭&甜宠&虐恋&穿越&重生', // 分类筛选 
    class_url:'nixi&tianchong&nuelian&chuanyue&chongsheng',
    class_parse: '.stui-header__menu&&li;a&&title;a&&href;.*/(.*?).html',
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
