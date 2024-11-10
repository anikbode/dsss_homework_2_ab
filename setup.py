from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Name of your package
    version="0.1",  # Version of your package
    packages=find_packages(),  # Automatically find your Python packages (including subfolders)
    install_requires=[  # List of external dependencies if any (leave empty if none)
        # 'some-package',  # Example: 'numpy', 'requests', etc.
    ],
    tests_require=['unittest'],  # List of test dependencies
    test_suite='tests',  # Location of your test suite
    long_description=open('README.md').read(),  # Read your README file for description
    long_description_content_type='text/markdown',  # Type of README file
    classifiers=[  # Metadata to categorize your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={  # If you want to make your package executable from the command line
        'console_scripts': [
            'math_quiz = DSSS_HOMEWORK_2_AB.math_quiz.math_quiz:main_function',  # Change this to your main function
        ],
    },
)
