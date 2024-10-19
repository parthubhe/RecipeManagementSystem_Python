document.addEventListener('DOMContentLoaded', function () {
    // Handle recipe card clicks to navigate to the recipe detail page
    const recipeCards = document.querySelectorAll('.card');

    recipeCards.forEach(function (card) {
        card.addEventListener('click', function () {
            const recipeId = this.dataset.id;
            window.location.href = `/recipe/${recipeId}`;
        });
    });

    // Handle previous and next recipe navigation
    const prevBtn = document.querySelector('#prevBtn');
    const nextBtn = document.querySelector('#nextBtn');

    if (prevBtn && nextBtn) {
        const currentRecipeId = parseInt(document.querySelector('#recipeDetail').dataset.id);

        function navigateRecipe(direction) {
            const newId = currentRecipeId + direction;
            window.location.href = `/recipe/${newId}`;
        }

        prevBtn.addEventListener('click', function () {
            navigateRecipe(-1); // Move to the previous recipe
        });

        nextBtn.addEventListener('click', function () {
            navigateRecipe(1); // Move to the next recipe
        });
    }
});
