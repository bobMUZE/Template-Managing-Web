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
            console.log(resultData)
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
        type: 'datetime',
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
            console.log(resultData)

            $('#apdex-chart > div').remove()
            $('.apdex-no').text(resultData["apdex"])
            $('.apdex-200').text(resultData['200'] + '%')
            $('.apdex-200-bar').css('width', resultData['200']*100 + '%');
            $('.apdex-400').text(resultData['400'] + '%')
            $('.apdex-400-bar').css('width', resultData['400']*100 + '%');

            $('.url-error-container').text(resultData['url'])
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
        offsetX: -10,
        offsetY: 0,
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

function changeLogProgress(time, progress, change){
    console.log(change)
    $.ajax({
        url: "./changeLogProgress/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'time': time, "progress": progress, "change": change},
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

function showLogModal(logdata){
    console.log(logdata)
    $('.log-modal-container #timestamp').text(logdata[0])
    $('.log-modal-container #url').text(logdata[1])
    $('.log-modal-container #xpath').text(logdata[2])
    $('.log-modal-container #status_code').text(logdata[3])
    $('.log-modal-container #request_time').text(logdata[4])
    $('.log-modal-container #module').text(logdata[5])
    $('.log-modal-container #detection').text(logdata[6])
    $('.log-modal-container #progress').text(logdata[7])
}