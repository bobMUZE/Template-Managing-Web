function change_period(period){
    getLoadData(period);
    getApdexData(period);
    getModuleData(period);
}


function getLoadData(period, target_id){
    $.ajax({
        url: "./getLoadData/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'period': period},
        success: function(resultData) {
            $('#load-time-chart > div').remove()
            loadTimeRefresh(resultData, target_id)

        //   $('#covid-change-data').text(changeRatio + ' ' + resultData['change_value'] + ' 명')
        //   changeCovidProgressbar(resultData['today_natDefCnt'], resultData['today_natDeathCnt'])
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // 에러 로그는 아래처럼 확인해볼 수 있다.
            console.log("covid data loading 에러\ncode : " + jqXHR.status + "\nerror message : " + jqXHR.responseText);
        }
    });
}

// @formatter:off
function loadTimeRefresh(result_data, target_id){
    var options = {
        series: [{
        name: 'request_time',
        data: result_data['request_time']
      }],
        chart: {
        type: 'area',
        stacked: false,
        height: 350,
        zoom: {
          type: 'x',
          enabled: true,
          autoScaleYaxis: true
        },
        toolbar: {
          autoSelected: 'zoom'
        }
      },
      dataLabels: {
        enabled: false
      },
      markers: {
        size: 0,
      },
      fill: {
        type: 'gradient',
        gradient: {
          shadeIntensity: 1,
          inverseColors: false,
          opacityFrom: 0.5,
          opacityTo: 0,
          stops: [0, 90, 100]
        },
      },
      xaxis: {
        categories: result_data['time'],
        type: 'category',
        datetimeUTC: false,
        datetimeFormatter: {
            year: 'yyyy',
            month: "MM 'yy",
            day: 'dd MM',
            hour: 'HH:mm',
        },
        labels: {
            format: 'yyyy-MM-d HH:mm',
          }
      },
      tooltip: {
        shared: false,
      }
    }

    var chart = new ApexCharts(document.getElementById('load-time-chart'), options);
    chart.render();
}
document.addEventListener("DOMContentLoaded", getLoadData(1, "load-time-chart"));
// @formatter:on


function getApdexData(period){
    $.ajax({
        url: "./getApdexData/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'period': period},
        success: function(resultData) {
            $('#apdex-chart > div').remove()
            $('.apdex-no').text(resultData["apdex"])
            $('.apdex-200').text(resultData['200']*100 + '%')
            $('.apdex-200-bar').css('width', resultData['200']*100 + '%');
            $('.apdex-400').text(resultData['400']*100 + '%')
            $('.apdex-400-bar').css('width', resultData['400']*100 + '%');

            error_urls = resultData['url'];

            error_urls.forEach(error_url => {
                url = error_url[0]
                code = error_url[1]
                
                var area = $('.url-error-table');
                var temp = document.createElement('tr');
                var td1 = document.createElement('td');
                var a_url = document.createElement('a');
                $(a_url).text(url);
                $(a_url).prop('href', url)
                $(a_url).prop('target', '_blank')
                $(td1).css('max-width', '260px');
                $(td1).css('font-size', '13px');
                var td2 = document.createElement('td');
                td2.className = "text-muted";
                $(td2).css('width', '40px');
                var h6 = document.createElement('h6');
                h6.className = "m-0";
                var span_chk = document.createElement('span');
                if(code == 400){
                    span_chk.className = "badge bg-danger";
                } else {
                    span_chk.className = "badge bg-warning";
                }
                $(span_chk).text(code);


                $(span_chk).appendTo(h6);
                $(h6).appendTo(td2);

                $(a_url).appendTo(td1);
                $(td1).appendTo(temp);
                $(td2).appendTo(temp);
    
                $(temp).appendTo(area);
            });

            // $('.url-error-container').text(resultData['url'])
            apdexRefresh(resultData)

        //   $('#covid-change-data').text(changeRatio + ' ' + resultData['change_value'] + ' 명')
        //   changeCovidProgressbar(resultData['today_natDefCnt'], resultData['today_natDeathCnt'])
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // 에러 로그는 아래처럼 확인해볼 수 있다.
            console.log("covid data loading 에러\ncode : " + jqXHR.status + "\nerror message : " + jqXHR.responseText);
        }
    });
}

function apdexRefresh(result_data){
    var options = {
        series: result_data['status_code'],
        chart: {
        height: 180,
        type: 'radialBar',
      },
      plotOptions: {
        radialBar: {
          offsetY: 0,
          startAngle: 0,
          endAngle: 270,
          hollow: {
            margin: 5,
            size: '30%',
            background: 'transparent',
            image: undefined,
          },
          dataLabels: {
            name: {
              show: false,
            },
            value: {
              show: false,
            }
          }
        }
      },
      colors: ['#1ab7ea', '#0084ff' ],
      labels: ['정상', '경고'],
      legend: {
        show: true,
        floating: true,
        fontSize: '10px',
        position: 'left',
        offsetX: -15,
        offsetY: -7,
        labels: {
          useSeriesColors: true,
        },
        markers: {
          size: 0
        },
        formatter: function(seriesName, opts) {
          return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
        },
        itemMargin: {
          vertical: 3
        }
      },
      responsive: [{
        breakpoint: 480,
        options: {
          legend: {
              show: false
          }
        }
      }]
      }

      var chart = new ApexCharts(document.getElementById('apdex-chart'), options);
      chart.render();
}
document.addEventListener("DOMContentLoaded", getApdexData(1));


// @formatter:off
function getModuleData(period){
    $.ajax({
        url: "./getModuleData/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'period': period},
        success: function(resultData) {
            $('#module-bar-chart > div').remove()
            moduleChartRefresh(resultData);

        //   $('#covid-change-data').text(changeRatio + ' ' + resultData['change_value'] + ' 명')
        //   changeCovidProgressbar(resultData['today_natDefCnt'], resultData['today_natDeathCnt'])
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // 에러 로그는 아래처럼 확인해볼 수 있다.
            console.log("covid data loading 에러\ncode : " + jqXHR.status + "\nerror message : " + jqXHR.responseText);
        }
    });
}

function moduleChartRefresh(result_data){
    var options = {
        series: [{
        name: 'XSS',
        data: result_data['xss']
      }, {
        name: '소스코드 위변조',
        data: result_data["code"]
      }, {
        name: 'URL 안정성 검사',
        data: result_data["url_safe"]
      }, {
        name: 'JQuery 위변조',
        data: result_data["jquery"]
      }, {
        name: 'iframe 도메인 탐지',
        data: result_data["iframe"]
      }, {
        name: 'ML_피싱 URL 탐지',
        data: result_data["phishing"]
      }],
        colors: ['#1ab7ea', '#6681C4', '#39539E', '#0A144B', '#A4FFFB'],
        chart: {
        type: 'bar',
        height: 200,
        stacked: true,
      },
      plotOptions: {
        bar: {
          horizontal: true,
        },
      },
      stroke: {
        width: 1,
        colors: ['#fff']
      },
      title: {
        text: '모듈 별 탐지 현황',
        style: {
            fontSize: '23px',
            fontFamily: 'Noto Sans KR',
            fontWeight: 700,
        },
      },
      xaxis: {
        categories: ["웹공격", "위변조 탐지", "ML- 파싱 URL 탐지"],

        style: {
            fontWeight: 700,
        },
      },
      yaxis: {
        title: {
          text: undefined
        },
      },
      fill: {
        opacity: 1
      },
      legend: {
        show: false,
      }
      }

    var chart = new ApexCharts(document.getElementById('module-bar-chart'), options);
    chart.render();
}
document.addEventListener("DOMContentLoaded", getModuleData(1));

function getLogProgressData(){
    $.ajax({
        url: "./getModuleData/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'period': period},
        success: function(resultData) {
            $('#module-bar-chart > div').remove()
            moduleChartRefresh(resultData);

        //   $('#covid-change-data').text(changeRatio + ' ' + resultData['change_value'] + ' 명')
        //   changeCovidProgressbar(resultData['today_natDefCnt'], resultData['today_natDeathCnt'])
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // 에러 로그는 아래처럼 확인해볼 수 있다.
            console.log("covid data loading 에러\ncode : " + jqXHR.status + "\nerror message : " + jqXHR.responseText);
        }
    });
}

function changeLogProgress(time, progress, change, module){
    $.ajax({
        url: "./changeLogProgress/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'time': time, "progress": progress, "change": change, "module": module},
        success: function(resultData) {
            location.reload();
            // reload 
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // 에러 로그는 아래처럼 확인해볼 수 있다.
            console.log("changeLogProgress data loading 에러\ncode : " + jqXHR.status + "\nerror message : " + jqXHR.responseText);
        }
    });
} 

function showEventLogModal(logdata){
    $('.log-modal-container #timestamp').text(logdata[11])
    var url_col = $('.log-modal-container #url')
    $(url_col).text("");
    var a_url = document.createElement('a');
    $(a_url).prop('href', logdata[2]);
    $(a_url).prop('target', '_blank')
    $(a_url).text(logdata[2]);
    $(a_url).appendTo(url_col);

    $('.log-modal-container #xpath').text(logdata[3])
    $('.log-modal-container #status_code').text(logdata[4])
    $('.log-modal-container #request_time').text(logdata[5])
    $('.log-modal-container #module').text(logdata[6])
    $('.log-modal-container #detection').text(logdata[7])
    $('.log-modal-container #progress').text(logdata[8])
    if (logdata[9] != -1){
        $('.log-modal-container .logdata').css('display', 'block');
        $('.log-modal-container .logdata *').css('display', 'block');

        var module_logs = logdata[9];
        // console.log(module_logs)
        $('.submodule-log-container *').remove()

        module_logs.forEach(module_log => {
            var area = $('.submodule-log-container');
            var temp = document.createElement('div');
            temp.className = "row";
            var hr = document.createElement('hr');
            hr.className = "col-12";
            $(hr).appendTo(temp);

            for (var key in module_log) { 
                // make div in here
                var submodule_dt = document.createElement('dt');
                submodule_dt.className = "col-3";
                $(submodule_dt).text(key);
                var submodule_dd = document.createElement('dd');
                submodule_dd.className = "col-9";
                submodule_dd.idName = "submodule";
                $(submodule_dd).text(module_log[key]);
                
                $(submodule_dt).appendTo(temp);
                $(submodule_dd).appendTo(temp);
            }
            $(temp).appendTo(area);
        });
        
        // $('.log-modal-container #submodule').text(logdata[8])

    } else {
        $('.log-modal-container .logdata').css('display', 'none');
        $('.log-modal-container .logdata *').css('display', 'none');
    }
}

function showLogModal(logdata){
    $('.log-modal-container #timestamp').text(logdata[0])
    var url_col = $('.log-modal-container #url')
    $(url_col).text("");
    var a_url = document.createElement('a');
    $(a_url).prop('href', logdata[1]);
    $(a_url).prop('target', '_blank')
    $(a_url).text(logdata[1]);
    $(a_url).appendTo(url_col);

    $('.log-modal-container #xpath').text(logdata[2])
    $('.log-modal-container #status_code').text(logdata[3])
    $('.log-modal-container #request_time').text(logdata[4])
    $('.log-modal-container #module').text(logdata[5])
    $('.log-modal-container #detection').text(logdata[6])
    $('.log-modal-container #progress').text(logdata[7])
    if (logdata[8] != -1){
        $('.log-modal-container .logdata').css('display', 'block');
        $('.log-modal-container .logdata *').css('display', 'block');

        var module_logs = logdata[8];
        $('.submodule-log-container *').remove()

        module_logs.forEach(module_log => {
            var area = $('.submodule-log-container');
            var temp = document.createElement('div');
            temp.className = "row";
            var hr = document.createElement('hr');
            hr.className = "col-12";
            $(hr).appendTo(temp);

            for (var key in module_log) { 
                // make div in here
                var submodule_dt = document.createElement('dt');
                submodule_dt.className = "col-3";
                $(submodule_dt).text(key);
                var submodule_dd = document.createElement('dd');
                submodule_dd.className = "col-9";
                submodule_dd.idName = "submodule";
                $(submodule_dd).text(module_log[key]);
                
                $(submodule_dt).appendTo(temp);
                $(submodule_dd).appendTo(temp);
            }
            $(temp).appendTo(area);
        });
        
        // $('.log-modal-container #submodule').text(logdata[8])

    } else {
        $('.log-modal-container .logdata').css('display', 'none');
        $('.log-modal-container .logdata *').css('display', 'none');
    }
}



function log_true_filter(){
    var is_true_checked = $("#log-table-true-btn").prop("checked");
    if(is_true_checked){
        $('.log-true').css("display", "none");
        $('#log-table-true-btn').attr( 'checked', false );
    } else {
        $('.log-true').css("display", "table-row");
        $('#log-table-true-btn').attr( 'checked', true );
    }
}

function log_false_filter(){
    var is_false_checked = $("#log-table-false-btn").prop("checked");
    if(is_false_checked){
        $('.log-false').css("display", "none");
        $('#log-table-false-btn').attr( 'checked', false );
    } else {
        $('.log-false').css("display", "table-row");
        $('#log-table-false-btn').attr( 'checked', true );
    }
}

document.addEventListener("DOMContentLoaded", log_true_filter());
document.addEventListener("DOMContentLoaded", log_false_filter());
