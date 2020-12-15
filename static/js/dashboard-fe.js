function getStatusCode(period){
    $.ajax({
        url: "./get_covid_data/",
        type: "get",
        dataType: "json",
        contentType: "application/json",
        data: {'period': period},
        success: function(resultData) {
          $('#covid-chart > div').css('display', 'none')
          old_chart_id = $('#covid-chart > div').attr('id')
          let element = document.getElementById(old_chart_id);
          if (element != null){
            element.outerHTML = '';
            delete element;
          }
                    
          covid_chart_refresh(resultData)
          $('#covid-last-data').text(resultData['today_natDefCnt']+"명")
          changeRatio = ""
          if (resultData['change_value'] > 0) {
            changeRatio = '+'
            $('.covid-trend-img').attr("src", "{% static 'img/trending-up.svg' %}");
          }
          else if (resultData['change_value'] = 0) {
            changeRatio = ''
          }
          else if (resultData['change_value'] < 0) {
            changeRatio = '-'
            $('#.covid-trend-img').attr("src", "{% static 'img/trending-down.svg' %}");
          }
          $('#covid-change-data').text(changeRatio + ' ' + resultData['change_value'] + ' 명')
          changeCovidProgressbar(resultData['today_natDefCnt'], resultData['today_natDeathCnt'])
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // 에러 로그는 아래처럼 확인해볼 수 있다. 
            console.log("covid data loading 에러\ncode : " + jqXHR.status + "\nerror message : " + jqXHR.responseText);
        }
    }); 
}