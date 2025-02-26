<template>
<div class="main-container">
    <div class="vault-container">
        <div class="vault chapter">
            <h3 class="title">{{ $t('main.my-safe') }}
                <img class="icon" src="@/assets/icons/safe-icon.svg" alt="">
            </h3>
            <div class="hr"></div>
        </div>
        <div class="password chapter">
            <h3 class="title">{{ $t('main.my-rights') }}
                <img class="icon" src="@/assets/icons/lock-icon.svg" alt="">
            </h3>
            <div class="hr"></div>
        </div>
    </div>

    <div class="info-container">
        <div class="header"></div>
    </div>

</div>  
</template>
  
<script embeded>
  
</script>


<style lang="scss" scoped>
    $shadow: var(--shadow);
    $accent: var(--accent-color);
    $secondary: var(--secondary-color);

    .main-container {
        background-color: white;
        overflow: hidden;
        border-radius: 20px;
        display: flex;
        width: calc(100% - 50px); // Корректируем ширину с учетом margin
        height: calc(100% - 50px); // Корректируем высоту с учетом margin
        box-shadow: $shadow 0px 0px 30px;
    }
    
    .info-container {
        width: 100%;
        height: 100%;

        
        
        .header{
            width: 100%;
            background-color: var(--gray-blue-color);
            height: 100px;
        }
        
    }


    .vault-container {
        background-color: $secondary;
        height: 100%;
        display: flex;
        width: 350px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        padding: 10px;
        box-sizing: border-box;

        .chapter {
            width: 100%;
            flex-grow: 1; // Позволяет элементам расти, занимая всё доступное место
            flex-basis: 0; // Начальная ширина элемента равна нулю (чтобы они росли пропорционально)
            border: var(--gray-light-color) 2px solid;
            border-radius: 10px;
            padding: 5px;
            
            align-items: center;
            flex-direction: column;
            display:flex ;
            box-sizing: border-box;

            
        .title {
            color: var(--white);
            justify-content: center;
            align-items: center;
            display: flex;
            width: 100%;
            height: 30px;
            font-family: "Akt";
            text-align: center;
            font-weight: 300;
            gap: 5px;

            .icon {
                height: 70%;
            }
            }
        
        
        }

        .hr {
    margin-top: 5px;
    width: 70%;
    height: 1px; /* Устанавливаем высоту линии */
    background-color: var(--white); /* Цвет фона для маски */
    border: none; /* Убираем стандартную границу hr */
    border-radius: 5px; /* Закругляем углы */
    mask-image: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 50%, rgba(0, 0, 0, 0) 100%); /* Маска */
    mask-size: 100% 100%; /* Размер маски */
    mask-repeat: no-repeat; /* Отключаем повтор маски */
    display: block; /* Убедимся, что элемент отображается как блок */
    margin-left: auto; /* Центрируем линию */
    margin-right: auto; /* Центрируем линию */
}

    }    

    

</style>