{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM37C7qcyG2c5NmqZeBM6kV",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/usman-codez/Number_Guessing-game/blob/main/Num_guessing.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2YpYXbcvp3jV",
        "outputId": "3596c5ed-36cc-4b16-863f-aba0d2cf99d6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your 1st choice number (1 to 20): 19\n",
            "High guess\n",
            "Enter your 2nd choice number (1 to 20):12\n",
            "High guess\n",
            "Both guess failed! The right number was 9\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "num_guess=random.randint(1,20)\n",
        "num1=int(input('Enter your 1st choice number (1 to 20): '))\n",
        "if num1==num_guess:\n",
        "    print('You won')\n",
        "\n",
        "elif num1<num_guess:\n",
        "  print('Low guess')\n",
        "\n",
        "else:\n",
        "  print('High guess')\n",
        "\n",
        "if num1!=num_guess:\n",
        "  num2=int(input('Enter your 2nd choice number (1 to 20):'))\n",
        "\n",
        "  if num2==num_guess:\n",
        "    print('You won')\n",
        "\n",
        "  elif num2<num_guess:\n",
        "    print('Low guess')\n",
        "\n",
        "  else:\n",
        "    print('High guess')\n",
        "\n",
        "if num1!=num_guess and num2!=num_guess:\n",
        "  print(f'Both guess failed! The right number was {num_guess}')\n",
        "\n"
      ]
    }
  ]
}