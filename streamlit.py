import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

SLU = [
    ["Relationships", "Significant other", "Time with partner, dates"],
    ["Relationships", "Family", "Engaging with kids, parents, siblings"],
    ["Relationships", "Friendship", "Time with friends"],
    [
        "Body, mind and spirituality",
        "Physical health/sports",
        "Exercise, physical therapy",
    ],
    [
        "Body, mind and spirituality",
        "Mental health/mindfulness",
        "Psycotherapy, meditation",
    ],
    [
        "Body, mind and spirituality",
        "Spirituality/faith",
        "Religious practice",
    ],
    [
        "Community and society",
        "Community/citizenship",
        "Membership in local clubs, jury duty",
    ],
    ["Community and society", "Societal engagement", "Volunteering, activism"],
    ["Job, learning and finances", "Job/career", "Work"],
    ["Job, learning and finances", "Education/learning", "Classes, training"],
    ["Job, learning and finances", "Finances", "Planning,investing"],
    [
        "Interests and entertainment",
        "Hobbies/interests",
        "Reading, collectibles",
    ],
    [
        "Interests and entertainment",
        "Online entertainment",
        "Social media, TV, gaming",
    ],
    [
        "Interests and entertainment",
        "Offline entertainment",
        "Vacations, theater, sporting events",
    ],
    ["Personal care", "Physiological needs", "Eating, sleeping"],
    ["Personal care", "Activities of daily living", "Commuting, housework"],
]

SLU = [
    ["Отношения", "Близкий человек", "Время вдвоем, свидания"],
    ["Отношения", "Семья", "Взаимодействие с детьми, родителями, братьями и сестрами"],
    ["Отношения", "Дружба", "Время с друзьями"],
    [
        "Тело, разум и духовность",
        "Физическое здоровье/спорт",
        "Физические упражнения, физиотерапия",
    ],
    [
        "Тело, разум и духовность",
        "Психическое здоровье/медитация",
        "Психотерапия, медитация",
    ],
    [
        "Тело, разум и духовность",
        "Духовность/вера",
        "Религиозная практика",
    ],
    [
        "Сообщество и общество",
        "Сообщество/гражданство",
        "Членство в местных клубах, участие в суде",
    ],
    ["Сообщество и общество", "Общественная активность", "Волонтерство, активизм"],
    ["Работа, обучение и финансы", "Работа/карьера", "Работа"],
    ["Работа, обучение и финансы", "Образование/обучение", "Курсы, тренинги"],
    ["Работа, обучение и финансы", "Финансы", "Планирование, инвестирование"],
    [
        "Интересы и развлечения",
        "Хобби/интересы",
        "Чтение, коллекционирование",
    ],
    [
        "Интересы и развлечения",
        "Онлайн-развлечения",
        "Социальные медиа, телевидение, игры",
    ],
    [
        "Интересы и развлечения",
        "Офлайн-развлечения",
        "Отпуск, театр, спортивные события",
    ],
    ["Личный уход", "Физиологические потребности", "Питание, сон"],
    ["Личный уход", "Активности ежедневной жизни", "Коммутирование, домашние дела"],
]


def check_hours_sum(session_state: dict) -> bool:
    sum_hours = sum(value for key, value in session_state.items() if "_hours" in key)
    hours_left = 168 - sum_hours
    return sum_hours > 168, hours_left


with st.expander("Источник"):
    st.write(
        "https://hbr.org/2023/12/use-strategic-thinking-to-create-the-life-you-want"
    )
    st.write("https://www.youtube.com/watch?v=dbiNhAZlXZk")

# st.write(st.session_state)
with st.expander("Описание метода"):
    st.write(
        """Компании часто используют анализ портфеля для оценки своих подразделений по ключевым параметрам, таким как рост рынка или доля, чтобы принимать решения о распределении капитала. Особенно известна BCG со своей матрицей роста и доли рынка размером 2x2.

Но каков эквивалент бизнес-юнита в жизни? Мы фокусируемся на шести стратегических областях жизни: отношениях; заботе о теле, уме и духе; общении в обществе; работе, обучении и финансах; интересах и развлечениях; а также личном уходе. Затем мы подразделяем эти шесть областей на 16 стратегических единиц жизни."""
    )
    st.image("BI_36_STRATEGIZE_YOUR_LIFE_KEY_AREAS_610-1200x1096.png")
    st.write(
        """И что же является эквивалентами капитальных затрат в жизни? Время, энергия и деньги. В неделе 168 часов. Как вы их расходуете? Вместе с близким человеком, с семьей, на работе, занимаясь спортом, в церкви, получая полноценный ночной отдых?

Взгляните на прошедший год, включая праздники, и оцените, сколько времени вы тратили на каждую из 16 стратегических единиц жизни в среднюю неделю. Когда деятельность попадает в несколько категорий, разделите время между ними. Например, если вы занимались бегом со своим близким человеком в течение одного часа в неделю, распределите полчаса на стратегическую единицу "Близкий человек" и полчаса на "Физическое здоровье/спорт". Затем оцените все 16 стратегических единиц по шкале от 0 до 10 в зависимости от их важности для вас. Затем оцените удовлетворение, которое вы получаете от каждой из них, по той же шкале."""
    )
st.write("Чтобы построить такой график, нужно заполнить значения ниже.")
st.image("example.png")
st.markdown(
    """Краткая инструкция по Оценке SLU:

1. Важность:

    * Оцените важность каждой стратегической единицы жизни (SLU) от 0 до 10. Насколько эта область важна для вашего благополучия?
2. Удовлетворенность:

    * Оцените уровень удовлетворенности каждой SLU от 0 до 10. Насколько вы удовлетворены текущим состоянием этой области?
3. Время в Неделю:

    * Укажите количество часов, которое вы тратите на каждую SLU в неделю. Обратите внимание на ограничение в 168 часов.
            
Подсказка: Сбалансируйте свои оценки, стремясь к равномерному распределению времени, и следите за ограничением по часам в неделю."""
)

for _ in range(7):
    st.write("\n")
# How significant is the SLU
for i, slu in enumerate(SLU):
    # slu example ["Personal care", "Activities of daily living", "Commuting, housework"]
    st.subheader(slu[1])
    st.write(slu[2])
    st.radio(
        "Важность",
        list(range(0, 11)),
        horizontal=True,
        key=slu[1] + "_Важность",
    )
    st.radio(
        "Удовлетворенность",
        list(range(0, 11)),
        horizontal=True,
        key=slu[1] + "_Удовлетворенность",
    )
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.number_input(
            "Часов в неделю",
            min_value=0,
            max_value=168,
            step=1,
            key=slu[1] + "_hours",
        )
    with col2:
        exceeded, hours_left = check_hours_sum(st.session_state)
        if exceeded:
            st.write(f"\nПревышено кол-во часов в неделю на {abs(hours_left)} часов.")
        else:
            st.write(f"\nОсталось {hours_left} часов до максимального кол-ва в неделю.")

    for _ in range(7):
        st.write("\n")


def create_df(session_state: dict) -> pd.DataFrame:
    categories = []
    subcategories = []
    values = []

    for key, value in session_state.items():
        category, subcategory = key.split("_")
        categories.append(category)
        subcategories.append(subcategory)
        values.append(value)

    # Создаем DataFrame
    df = pd.DataFrame(
        {"Category": categories, "Subcategory": subcategories, "Value": values}
    )

    # Преобразуем DataFrame, используя значения из столбцов в качестве индекса и столбцов
    df = df.pivot(index="Category", columns="Subcategory", values="Value")

    # df["Важность"] = np.random.randint(0, 11, df.shape[0])
    # df["Удовлетворение"] = np.random.randint(0, 11, df.shape[0])
    # df["hours"] = np.random.randint(0, 168, df.shape[0])

    df["scaled_hours"] = df["hours"] * 10
    df = df.reset_index()
    return df


if st.button("Создать график"):
    df = create_df(st.session_state)
    # chart = (
    #     alt.Chart(df)
    #     .mark_point()
    #     .encode(x="satisfaction", y="importance", size="hours")
    # )

    chart = (
        alt.Chart(df)
        .mark_point(filled=False)
        .encode(
            x=alt.X("Удовлетворенность", scale=alt.Scale(domain=[-1, 11])),
            y=alt.Y("Важность", scale=alt.Scale(domain=[-1, 11])),
            size=alt.Size(
                "scaled_hours",
                # scale=alt.Scale(domain=[0, 168]),
                legend=None,
            ),
            opacity=alt.value(0.5),  # Устанавливаем полупрозрачность
            color=alt.Color("Category", legend=None),
            tooltip=["Category", "hours"],
        )
        .properties(width=600, height=600)
        # .configure_legend(disable=True)
    )

    horizontal_rule = (
        alt.Chart(pd.DataFrame({"Важность": [5]}))
        .mark_rule(color="blue")
        .encode(y="Важность")
    )

    # Добавление вертикальной линии в значении 5
    vertical_rule = (
        alt.Chart(pd.DataFrame({"Удовлетворенность": [5]}))
        .mark_rule(color="blue")
        .encode(x="Удовлетворенность")
    )

    # Комбинирование графика с линиями

    combined_chart = alt.layer(chart, horizontal_rule, vertical_rule)

    st.altair_chart(combined_chart, use_container_width=False)
    st.caption("Наводя курсор на отметку, вы увидете ее название.")

    with st.expander("Интерпретация"):
        st.write(
            """В верхнем левом квадранте вы найдете стратегические единицы жизни (SLU) с высокой важностью и низким уровнем удовлетворенности. Это области повышенной срочности, поскольку вы глубоко заботитесь об этих занятиях, но не уделяете им достаточно внимания, чтобы извлечь максимальную выгоду. 

Стратегические единицы в верхнем правом квадранте также заслуживают внимания: вы хотите продолжать уделять значительное время и энергию вашим наиболее важным и удовлетворительным занятиям, и вложить меньше в те, которые менее важны (нижний левый и правый квадранты).

Наконец, взгляните на весь ваш 2x2 и спросите себя: соответствует ли мой текущий портфель стратегических единиц жизни моей цели и моему видению? Приближает ли он меня к тому, как я определяю прекрасную жизнь? Где я могу сэкономить и перераспределить свое время? Точно так же, как в стратегических проектах корпоративной стратегии, вы хотите установить высокоуровневые приоритеты — вместо детального плана — для вложений вашего времени, энергии и денег."""
        )
