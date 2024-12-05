// 지도 초기화 후 클릭 이벤트 처리
window.onload = function() {
  simplemaps_countrymap.state_click = function(state_id) {
      // 클릭된 지역에 따라 다른 동작을 실행
      if (state_id === 'KR11') {
          alert('서울을 클릭했습니다!');
          // 예: 서울을 클릭했을 때 색상 변경
          document.getElementById('KR11').style.fill = "#ff0000";  // 서울 색상 빨간색으로 변경
      } else if (state_id === 'KR26') {
          alert('부산을 클릭했습니다!');
          // 예: 부산을 클릭했을 때 색상 변경
          document.getElementById('KR26').style.fill = "#0000ff";  // 부산 색상 파란색으로 변경
      }
  };
};
