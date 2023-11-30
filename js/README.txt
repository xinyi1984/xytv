把zip文件解壓縮到安卓設備的/sdcard/tvbox/JS/目錄
複製lib/tokentemplate.json成爲lib/tokenm.json，并填寫必要的内容

格式説明：
{
"token":"這裏填寫阿里云盤的32位token，也可以不填寫，在播放阿里云盤内容時會彈出窗口，點擊QrCode，用阿里云盤app掃碼",
"open_token":"這裏填寫通過alist申請的280位aliyun openapi token，也可以不寫，會自動隱藏轉存原畫",
"thread_limit":32, //這裏是GO代理的并發協程數或java代理的并發綫程數，并非越大越好，最高到64足以
"vod_flags":"4k|4kz|auto", //這裏是播放阿里雲的畫質選項，4k代表不轉存原畫（GO原畫），4kz代表轉存原畫,其他都代表預覽畫質,可選的預覽畫質包括qhd,fhd,hd,sd,ld
"quark_flags":"4kz|auto", //這裏是播放夸克網盤的畫質選項，4kz代表轉存原畫（GO原畫），其他都代表轉碼畫質,可選的預覽畫質包括4k,2k,super,high,low,normal
"aliproxy":"這裏填寫外部的加速代理，用於在盒子性能不夠的情況下，使用外部的加速代理來加速播放，可以不填寫",
"proxy":"這裏填寫用於科學上網的地址，連接openapi或某些資源站可能會需要用到，可以不填寫",
"open_api_url":"https://api.xhofe.top/alist/ali_open/", //這是alist的openapi接口地址
"danmu":true,//是否全局開啓阿里云盤所有csp的彈幕支持
"quark_danmu":true,//是否全局開啓夸克網盤的所有csp的彈幕支持
"quark_cookie":"這裏填寫通過https://pan.quark.cn網站獲取到的cookie，會很長，全數填入即可。"
}
