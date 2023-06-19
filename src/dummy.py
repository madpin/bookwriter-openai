from model import Book, Chapter, Subchapter, Section

book = Book(
    # id=55,
    title="Machine Learning with Python",
    subtitle="Using Scikit-Learn and TensorFlow",
    description="This book covers machine learning concepts and their implementation in Python using Scikit-Learn and TensorFlow.",
    short_description="A book on machine learning with Python",
    chapters=[
        Chapter(
            id=1,
            title="Introduction to Machine Learning",
            description="This chapter covers the basics of machine learning, types of machine learning, supervised and unsupervised learning, and important terminologies used in machine learning.",
            short_description="Introduction to machine learning",
            subchapters=[
                Subchapter(
                    id=1,
                    title="What is Machine Learning?",
                    description="An overview of the concept of machine learning.",
                    short_description="What is machine learning?",
                    sections=[
                        Section(
                            id=1,
                            title="Section Title",
                            description="Short Description",
                            content="Content..."
                        )
                    ]
                ),
                Subchapter(
                    id=3,
                    title="Machine Learning Algorithms",
                    description="An overview of popular machine learning algorithms.",
                    short_description="Machine learning algorithms",
                    sections=[
                        Section(
                            id=1,
                            title="Section Title",
                            description="Short Description",
                            content="Content..."
                        )
                    ]
                ),
            ],
        ),
        Chapter(
            id=2,
            title="Python for Machine Learning",
            description="This chapter covers the basics of Python programming and how to use Python for machine learning.",
            short_description="Python for machine learning",
            subchapters=[
                Subchapter(
                    id=1,
                    title="Python Basics",
                    description="A quick overview of Python data types, operators, control flows, and functions.",
                    short_description="Python basics",
                    sections=[
                        Section(
                            id=1,
                            title="Section Title",
                            description="Short Description",
                            content="Content..."
                        )
                    ]
                ),
                Subchapter(
                    id=2,
                    title="NumPy for Machine Learning",
                    description="Using NumPy for efficient array processing in machine learning.",
                    short_description="NumPy for machine learning",
                    sections=[
                        Section(
                            id=1,
                            title="Section Title",
                            description="Short Description",
                            content="Content..."
                        )
                    ]
                ),
                Subchapter(
                    id=3,
                    title="pandas for Data Analysis",
                    description="Using pandas for data analysis and manipulation.",
                    short_description="pandas for data analysis",
                    sections=[
                        Section(
                            id=1,
                            title="Section Title",
                            description="Short Description",
                            content="Content..."
                        )
                    ]
                ),
            ],
        ),
    ],
)
