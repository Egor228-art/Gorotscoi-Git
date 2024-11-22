<script>
        function checkEnter(event) {
            if (event.key === 'Enter') {
                document.querySelector('form').submit();
            }
        }

        function handleSubmit() {
            const input = document.getElementById('query');
            if (input.value.trim() === '') {
                return false; // Не отправляем форму, если поле пустое
            }
            return true; // Отправляем форму
        }
</script>