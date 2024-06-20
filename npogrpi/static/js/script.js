document.addEventListener('DOMContentLoaded', function() {
    const track = document.querySelector('.carousel-track');
    const prevButton = document.querySelector('.left-button');
    const nextButton = document.querySelector('.right-button');
    let currentIndex = 0;

    function moveToIndex(index) {
        const width = track.children[0].getBoundingClientRect().width;
        track.style.transform = 'translateX(' + (-width * index) + 'px)';
    }

    nextButton.addEventListener('click', function() {
        currentIndex++;
        if (currentIndex >= track.children.length) {
            currentIndex = 0; // или можно убрать эту строку для остановки на последнем логотипе
        }
        moveToIndex(currentIndex);
    });

    prevButton.addEventListener('click', function() {
        currentIndex--;
        if (currentIndex < 0) {
            currentIndex = track.children.length - 1; // или можно установить currentIndex = 0 для остановки на первом логотипе
        }
        moveToIndex(currentIndex);
    });
});
