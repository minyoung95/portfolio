document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelector(".slides");
  const slide = document.querySelectorAll(".slide");
  const prevBtn = document.querySelector(".prev");
  const nextBtn = document.querySelector(".next");

  let currentIndex = 0;
  const totalSlides = slide.length;

  // 슬라이드 이동 함수
  function moveToSlide(index) {
      slides.style.transform = `translateX(-${index * 100}%)`;
  }

  // 이전 버튼 클릭
  prevBtn.addEventListener("click", () => {
      currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
      moveToSlide(currentIndex);
  });

  // 다음 버튼 클릭
  nextBtn.addEventListener("click", () => {
      currentIndex = (currentIndex + 1) % totalSlides;
      moveToSlide(currentIndex);
  });

  // 자동 슬라이드 기능
  let autoSlide = setInterval(() => {
      currentIndex = (currentIndex + 1) % totalSlides;
      moveToSlide(currentIndex);
  }, 3000);

  // 슬라이더에 마우스 올리면 일시 정지
  const sliderContainer = document.querySelector(".slider-container");
  sliderContainer.addEventListener("mouseenter", () => clearInterval(autoSlide));
  sliderContainer.addEventListener("mouseleave", () => {
      autoSlide = setInterval(() => {
          currentIndex = (currentIndex + 1) % totalSlides;
          moveToSlide(currentIndex);
      }, 3000);
  });
});
