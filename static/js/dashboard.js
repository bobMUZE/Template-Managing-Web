
// @formatter:off
document.addEventListener("DOMContentLoaded", function () {
window.ApexCharts && (new ApexCharts(document.getElementById('chart-line-stroke'), {
    chart: {
        type: "line",
        fontFamily: 'inherit',
        height: 160,
        parentHeightOffset: 0,
        toolbar: {
            show: false,
        },
        animations: {
            enabled: false
        },
    },
    fill: {
        opacity: 1,
    },
    stroke: {
        width: 2,
        lineCap: "round",
        curve: "straight",
    },
    series: [{
        name: "Development",
        data: [8, 10, 11, 12, 20, 27, 30]
    },{
        name: "Marketing",
        data: [3, 16, 17, 19, 20, 30, 30]
    },{
        name: "Sales",
        data: [7, 10, 11, 18, 18, 18, 24]
    }],
    grid: {
        padding: {
            top: -20,
            right: 0,
            left: -4,
            bottom: -4
        },
        strokeDashArray: 4,
    },
    xaxis: {
        labels: {
            padding: 0
        },
        tooltip: {
            enabled: false
        },
        categories: ["2013", "2014", "2015", "2016", "2017", "2018", "2019"],
    },
    yaxis: {
        labels: {
            padding: 4
        },
    },
    colors: ["#ff922b", "#206bc4", "#5eba00"],
    legend: {
        show: false,
    },
})).render();
});
// @formatter:on



// @formatter:off
document.addEventListener("DOMContentLoaded", function () {
    window.ApexCharts && (new ApexCharts(document.getElementById('chart-line-stroke2'), {
        chart: {
            type: "line",
            fontFamily: 'inherit',
            height: 160,
            parentHeightOffset: 0,
            toolbar: {
                show: false,
            },
            animations: {
                enabled: false
            },
        },
        fill: {
            opacity: 1,
        },
        stroke: {
            width: 2,
            lineCap: "round",
            curve: "straight",
        },
        series: [{
            name: "Development",
            data: [8, 10, 11, 12, 20, 27, 30]
        },{
            name: "Marketing",
            data: [3, 16, 17, 19, 20, 30, 30]
        },{
            name: "Sales",
            data: [7, 10, 11, 18, 18, 18, 24]
        }],
        grid: {
            padding: {
                top: -20,
                right: 0,
                left: -4,
                bottom: -4
            },
            strokeDashArray: 4,
        },
        xaxis: {
            labels: {
                padding: 0
            },
            tooltip: {
                enabled: false
            },
            categories: ["2013", "2014", "2015", "2016", "2017", "2018", "2019"],
        },
        yaxis: {
            labels: {
                padding: 4
            },
        },
        colors: ["#ff922b", "#206bc4", "#5eba00"],
        legend: {
            show: false,
        },
    })).render();
    });
    // @formatter:on




// @formatter:off
document.addEventListener("DOMContentLoaded", function () {
    window.ApexCharts && (new ApexCharts(document.getElementById('chart-line-stroke3'), {
        chart: {
            type: "line",
            fontFamily: 'inherit',
            height: 160,
            parentHeightOffset: 0,
            toolbar: {
                show: false,
            },
            animations: {
                enabled: false
            },
        },
        fill: {
            opacity: 1,
        },
        stroke: {
            width: 2,
            lineCap: "round",
            curve: "straight",
        },
        series: [{
            name: "Development",
            data: [8, 10, 11, 12, 20, 27, 30]
        },{
            name: "Marketing",
            data: [3, 16, 17, 19, 20, 30, 30]
        },{
            name: "Sales",
            data: [7, 10, 11, 18, 18, 18, 24]
        }],
        grid: {
            padding: {
                top: -20,
                right: 0,
                left: -4,
                bottom: -4
            },
            strokeDashArray: 4,
        },
        xaxis: {
            labels: {
                padding: 0
            },
            tooltip: {
                enabled: false
            },
            categories: ["2013", "2014", "2015", "2016", "2017", "2018", "2019"],
        },
        yaxis: {
            labels: {
                padding: 4
            },
        },
        colors: ["#ff922b", "#206bc4", "#5eba00"],
        legend: {
            show: false,
        },
    })).render();
    });
    // @formatter:on


// @formatter:off
document.addEventListener("DOMContentLoaded", function () {
    window.ApexCharts && (new ApexCharts(document.getElementById('chart-total-sales'),     {
        series: [76, 67, 61],
        chart: {
        height: 250,
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
      colors: ['#1ab7ea', '#0084ff', '#39539E' ],
      labels: ['정상', '경고', '오류'],
      legend: {
        show: true,
        floating: true,
        fontSize: '13px',
        position: 'left',
        offsetX: 20,
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
      })).render();
});
// @formatter:on


// @formatter:off
document.addEventListener("DOMContentLoaded", function () {
    var options ={
        series: [{
        name: 'PRODUCT A',
        data: [44, 55, 41, 67, 22, 43]
      }, {
        name: 'PRODUCT B',
        data: [91, 68, 25, 2, 5, 33]
      }],
        chart: {
        type: 'bar',
        height: 160,
        stacked: true,
        toolbar: {
          show: true
        },
        zoom: {
          enabled: true
        }
      },
      responsive: [{
        breakpoint: 480,
        options: {
          legend: {
            position: 'bottom',
            offsetX: -10,
            offsetY: 0
          }
        }
      }],
      plotOptions: {
        bar: {
          horizontal: false,
        },
      },
      xaxis: {
        type: 'category',
        tickAmount: 3,
        tickPlacement: 'on',
        categories: [['2020-12-13', '13:02:55.948'],'2020-12-13T13:02:55.948', '2020-12-13T13:02:56.722', '2020-12-13T13:02:56.726', '2020-12-13T13:02:57.802', '2020-12-13T13:02:58.622', '2020-12-13T13:03:03.531'
        ],
        labels: {
            rotate: 0
          }
      },

      tooltip: {
        x: {
            show: true,
            format: 'yyyy-MM-dd HH:mm:ss.fff',
        },
      },
      legend: {
        position: 'right',
        offsetY: 40
      },
      fill: {
        opacity: 1
      }
      }

    var chart = new ApexCharts(document.querySelector("#chart-completion-tasks9"), options);
        chart.render();
});
// @formatter:on


// @formatter:off
document.addEventListener("DOMContentLoaded", function () {
    window.ApexCharts && (new ApexCharts(document.getElementById('module-bar-chart'), {
        series: [{
        name: 'Marine Sprite',
        data: [44, 55, 41]
      }, {
        name: 'Striking Calf',
        data: [53, 32, 33]
      }, {
        name: 'Tank Picture',
        data: [12, 17, 11]
      }, {
        name: 'Bucket Slope',
        data: [9, 7, 5]
      }, {
        name: 'Reborn Kid',
        data: [25, 12, 19]
      }],
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
        labels: {
          formatter: function (val) {
            return val + "K"
          }
        }
      },
      yaxis: {
        title: {
          text: undefined
        },
      },
      tooltip: {
        y: {
          formatter: function (val) {
            return val + "K"
          }
        }
      },
      fill: {
        opacity: 1
      },
      legend: {
        show: false,
      }
      })).render();
});
// @formatter:on