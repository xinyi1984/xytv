把zip文件解壓縮到安卓設備的/sdcard/tvbox/JS/目錄
複製lib/tokentemplate.json成爲lib/tokenm.json，并填寫必要的内容

特別警告：據傳阿里要求使用者不得使用多綫程加速方式使用阿里云盤資源，若并發鏈接數超過10有可能導致被限制訪問或封禁帳號的處理，所以下方綫程限制設置超過10所需承擔的風險請使用者自行斟酌。

格式説明：
{
"token":"這裏填寫阿里云盤的32位token，也可以不填寫，在播放阿里云盤内容時會彈出窗口，點擊QrCode，用阿里云盤app掃碼",
"open_token":"這裏填寫通過alist申請的280位aliyun openapi token，也可以不寫，會自動隱藏轉存原畫",
"thread_limit":32, //這裏是阿里云盤的GO代理的并發協程數或java代理的并發綫程數，若遇到賬號被限制并發數，請將此數值改爲10
"is_vip":false, //是否是阿里云盤的VIP用戶，設置為true后，可以降低上方thread_limit的數量, 會提高多綫程加載效率。 注意! 非阿里雲盤VIP强行設置為true會有反效果.  注意2:因目前阿里云盤非VIP用戶轉存后的多綫播放效率已經不如GO極速播放，因此若此項設爲false會自動隱去"轉存原畫"
"quark_thread_limit":32, //這裏是夸克網盤GO代理的并發協程數或java代理的并發綫程數，若遇到賬號被限制並發數，請將此數值改爲10
"quark_is_vip":false, //是否是夸克網盤的VIP用戶，設置為true后，可以降低上方quark_thread_limit的數量, 會提高多綫程加載效率。注意！非夸克網盤VIP强行設置為true會有反效果.
"vod_flags":"4k|4kz|auto", //這裏是播放阿里雲的畫質選項，4k代表不轉存原畫（GO原畫），4kz代表轉存原畫,其他都代表預覽畫質,可選的預覽畫質包括qhd,fhd,hd,sd,ld，
"quark_flags":"4kz|auto", //這裏是播放夸克網盤的畫質選項，4kz代表轉存原畫（GO原畫），其他都代表轉碼畫質,可選的預覽畫質包括4k,2k,super,high,low,normal
"aliproxy":"這裏填寫外部的加速代理，用於在盒子性能不夠的情況下，使用外部的加速代理來加速播放，可以不填寫",
"proxy":"這裏填寫用於科學上網的地址，連接openapi或某些資源站可能會需要用到，可以不填寫",
"open_api_url":"https://api.xhofe.top/alist/ali_open/", //這是alist的openapi接口地址
"danmu":true,//是否全局開啓阿里云盤所有csp的彈幕支持，聚合類CSP仍需單獨設置，例如Wogg, Wobg
"quark_danmu":true,//是否全局開啓夸克網盤的所有csp的彈幕支持, 聚合類CSP仍需單獨設置，例如Wogg, Wobg
"quark_cookie":"這裏填寫通過https://pan.quark.cn網站獲取到的cookie，會很長，全數填入即可。"
}
