{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Analisis sobre videojuegos"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Carga de datos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tconst</th>\n",
       "      <th>titleType</th>\n",
       "      <th>primaryTitle</th>\n",
       "      <th>originalTitle</th>\n",
       "      <th>isAdult</th>\n",
       "      <th>startYear</th>\n",
       "      <th>endYear</th>\n",
       "      <th>runtimeMinutes</th>\n",
       "      <th>genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>82526</th>\n",
       "      <td>tt0084376</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>0</td>\n",
       "      <td>1982</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Crime,Mystery</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>84081</th>\n",
       "      <td>tt0085982</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Many Roads to Murder</td>\n",
       "      <td>MysteryDisc: Many Roads to Murder</td>\n",
       "      <td>0</td>\n",
       "      <td>1983</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Crime,Mystery</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>102636</th>\n",
       "      <td>tt0105000</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>0</td>\n",
       "      <td>1992</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Horror,Mystery</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>107360</th>\n",
       "      <td>tt0109865</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Gabriel Knight: Sins of the Fathers</td>\n",
       "      <td>Gabriel Knight: Sins of the Fathers</td>\n",
       "      <td>0</td>\n",
       "      <td>1993</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Drama,Horror</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>107752</th>\n",
       "      <td>tt0110267</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>King's Quest VII: The Princeless Bride</td>\n",
       "      <td>King's Quest VII: The Princeless Bride</td>\n",
       "      <td>0</td>\n",
       "      <td>1994</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Fantasy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           tconst  titleType                            primaryTitle  \\\n",
       "82526   tt0084376  videoGame            MysteryDisc: Murder, Anyone?   \n",
       "84081   tt0085982  videoGame       MysteryDisc: Many Roads to Murder   \n",
       "102636  tt0105000  videoGame                              Night Trap   \n",
       "107360  tt0109865  videoGame     Gabriel Knight: Sins of the Fathers   \n",
       "107752  tt0110267  videoGame  King's Quest VII: The Princeless Bride   \n",
       "\n",
       "                                 originalTitle  isAdult startYear endYear  \\\n",
       "82526             MysteryDisc: Murder, Anyone?        0      1982      \\N   \n",
       "84081        MysteryDisc: Many Roads to Murder        0      1983      \\N   \n",
       "102636                              Night Trap        0      1992      \\N   \n",
       "107360     Gabriel Knight: Sins of the Fathers        0      1993      \\N   \n",
       "107752  King's Quest VII: The Princeless Bride        0      1994      \\N   \n",
       "\n",
       "       runtimeMinutes                    genres  \n",
       "82526              \\N   Adventure,Crime,Mystery  \n",
       "84081              \\N   Adventure,Crime,Mystery  \n",
       "102636             \\N  Adventure,Horror,Mystery  \n",
       "107360             \\N    Adventure,Drama,Horror  \n",
       "107752             \\N         Adventure,Fantasy  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "basics = pd.read_csv(\"title.basics.tsv\", sep = \"\\t\")\n",
    "ratings = pd.read_csv(\"title.ratings.tsv\", sep = \"\\t\") \n",
    "\n",
    "videojuegos = basics[basics[\"titleType\"] == \"videoGame\"].copy()\n",
    "\n",
    "\n",
    "videojuegos.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Union de dataframes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tconst</th>\n",
       "      <th>titleType</th>\n",
       "      <th>primaryTitle</th>\n",
       "      <th>originalTitle</th>\n",
       "      <th>isAdult</th>\n",
       "      <th>startYear</th>\n",
       "      <th>endYear</th>\n",
       "      <th>runtimeMinutes</th>\n",
       "      <th>genres</th>\n",
       "      <th>averageRating</th>\n",
       "      <th>numVotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>tt0084376</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>0</td>\n",
       "      <td>1982</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Crime,Mystery</td>\n",
       "      <td>5.8</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>tt0085982</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Many Roads to Murder</td>\n",
       "      <td>MysteryDisc: Many Roads to Murder</td>\n",
       "      <td>0</td>\n",
       "      <td>1983</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Crime,Mystery</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tt0105000</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>0</td>\n",
       "      <td>1992</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Horror,Mystery</td>\n",
       "      <td>6.2</td>\n",
       "      <td>434.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>tt0109865</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Gabriel Knight: Sins of the Fathers</td>\n",
       "      <td>Gabriel Knight: Sins of the Fathers</td>\n",
       "      <td>0</td>\n",
       "      <td>1993</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Drama,Horror</td>\n",
       "      <td>8.9</td>\n",
       "      <td>820.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>tt0110267</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>King's Quest VII: The Princeless Bride</td>\n",
       "      <td>King's Quest VII: The Princeless Bride</td>\n",
       "      <td>0</td>\n",
       "      <td>1994</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Fantasy</td>\n",
       "      <td>7.6</td>\n",
       "      <td>229.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      tconst  titleType                            primaryTitle  \\\n",
       "0  tt0084376  videoGame            MysteryDisc: Murder, Anyone?   \n",
       "1  tt0085982  videoGame       MysteryDisc: Many Roads to Murder   \n",
       "2  tt0105000  videoGame                              Night Trap   \n",
       "3  tt0109865  videoGame     Gabriel Knight: Sins of the Fathers   \n",
       "4  tt0110267  videoGame  King's Quest VII: The Princeless Bride   \n",
       "\n",
       "                            originalTitle  isAdult startYear endYear  \\\n",
       "0            MysteryDisc: Murder, Anyone?        0      1982      \\N   \n",
       "1       MysteryDisc: Many Roads to Murder        0      1983      \\N   \n",
       "2                              Night Trap        0      1992      \\N   \n",
       "3     Gabriel Knight: Sins of the Fathers        0      1993      \\N   \n",
       "4  King's Quest VII: The Princeless Bride        0      1994      \\N   \n",
       "\n",
       "  runtimeMinutes                    genres  averageRating  numVotes  \n",
       "0             \\N   Adventure,Crime,Mystery            5.8      42.0  \n",
       "1             \\N   Adventure,Crime,Mystery            NaN       NaN  \n",
       "2             \\N  Adventure,Horror,Mystery            6.2     434.0  \n",
       "3             \\N    Adventure,Drama,Horror            8.9     820.0  \n",
       "4             \\N         Adventure,Fantasy            7.6     229.0  "
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = videojuegos.merge(ratings, on = \"tconst\", how = \"left\")\n",
    "\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Limpieza básica"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tconst</th>\n",
       "      <th>titleType</th>\n",
       "      <th>primaryTitle</th>\n",
       "      <th>originalTitle</th>\n",
       "      <th>isAdult</th>\n",
       "      <th>startYear</th>\n",
       "      <th>endYear</th>\n",
       "      <th>runtimeMinutes</th>\n",
       "      <th>genres</th>\n",
       "      <th>averageRating</th>\n",
       "      <th>numVotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>tt0084376</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>0</td>\n",
       "      <td>1982</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Crime,Mystery</td>\n",
       "      <td>5.8</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tt0105000</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>0</td>\n",
       "      <td>1992</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Horror,Mystery</td>\n",
       "      <td>6.2</td>\n",
       "      <td>434.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>tt0109865</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Gabriel Knight: Sins of the Fathers</td>\n",
       "      <td>Gabriel Knight: Sins of the Fathers</td>\n",
       "      <td>0</td>\n",
       "      <td>1993</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Drama,Horror</td>\n",
       "      <td>8.9</td>\n",
       "      <td>820.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>tt0110267</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>King's Quest VII: The Princeless Bride</td>\n",
       "      <td>King's Quest VII: The Princeless Bride</td>\n",
       "      <td>0</td>\n",
       "      <td>1994</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure,Fantasy</td>\n",
       "      <td>7.6</td>\n",
       "      <td>229.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>tt0110714</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Off-World Interceptor</td>\n",
       "      <td>Off-World Interceptor</td>\n",
       "      <td>0</td>\n",
       "      <td>1994</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Action,Comedy,Sci-Fi</td>\n",
       "      <td>3.7</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      tconst  titleType                            primaryTitle  \\\n",
       "0  tt0084376  videoGame            MysteryDisc: Murder, Anyone?   \n",
       "2  tt0105000  videoGame                              Night Trap   \n",
       "3  tt0109865  videoGame     Gabriel Knight: Sins of the Fathers   \n",
       "4  tt0110267  videoGame  King's Quest VII: The Princeless Bride   \n",
       "5  tt0110714  videoGame                   Off-World Interceptor   \n",
       "\n",
       "                            originalTitle  isAdult startYear endYear  \\\n",
       "0            MysteryDisc: Murder, Anyone?        0      1982      \\N   \n",
       "2                              Night Trap        0      1992      \\N   \n",
       "3     Gabriel Knight: Sins of the Fathers        0      1993      \\N   \n",
       "4  King's Quest VII: The Princeless Bride        0      1994      \\N   \n",
       "5                   Off-World Interceptor        0      1994      \\N   \n",
       "\n",
       "  runtimeMinutes                    genres  averageRating  numVotes  \n",
       "0             \\N   Adventure,Crime,Mystery            5.8      42.0  \n",
       "2             \\N  Adventure,Horror,Mystery            6.2     434.0  \n",
       "3             \\N    Adventure,Drama,Horror            8.9     820.0  \n",
       "4             \\N         Adventure,Fantasy            7.6     229.0  \n",
       "5             \\N      Action,Comedy,Sci-Fi            3.7      11.0  "
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Eliminar duplicados\n",
    "df = df.drop_duplicates()\n",
    "\n",
    "# \"Eliminar nulos\"\n",
    "df = df[df[\"startYear\"] != \"\\\\N\"]\n",
    "df = df[df[\"genres\"] != \"\\\\N\"]\n",
    "\n",
    "df = df.dropna(subset = [\"averageRating\"])\n",
    "df = df.dropna(subset = [\"genres\"])\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Promedio por año"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "startYear\n",
       "2022    6.751168\n",
       "2023    6.867573\n",
       "2024    6.940257\n",
       "2025    7.049845\n",
       "2026    6.462500\n",
       "Name: averageRating, dtype: float64"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings_anuales = df.groupby(\"startYear\")[\"averageRating\"].mean()\n",
    "\n",
    "ratings_anuales.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "ratings_anuales.plot()\n",
    "plt.xlabel(\"Año\")\n",
    "plt.ylabel(\"Rating promedio\")\n",
    "plt.title(\"Evolución del rating promedio por año\")\n",
    "plt.show()    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Los ratings presentan alta variabilidad en las primeras décadas debido al bajo volumen de registros. A partir de los años 70 se observa un crecimiento sostenido en la calidad percibida, coincidiendo con la expansión de la industria. Desde el 2000, los ratings se estabilizan, lo que sugiere madurez del sector y estándares de calidad más consistentes."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Análisis por genero"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>tconst</th>\n",
       "      <th>titleType</th>\n",
       "      <th>primaryTitle</th>\n",
       "      <th>originalTitle</th>\n",
       "      <th>isAdult</th>\n",
       "      <th>startYear</th>\n",
       "      <th>endYear</th>\n",
       "      <th>runtimeMinutes</th>\n",
       "      <th>genres</th>\n",
       "      <th>averageRating</th>\n",
       "      <th>numVotes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>tt0084376</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>0</td>\n",
       "      <td>1982</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>5.8</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>tt0084376</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>0</td>\n",
       "      <td>1982</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Crime</td>\n",
       "      <td>5.8</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>tt0084376</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>MysteryDisc: Murder, Anyone?</td>\n",
       "      <td>0</td>\n",
       "      <td>1982</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Mystery</td>\n",
       "      <td>5.8</td>\n",
       "      <td>42.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tt0105000</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>0</td>\n",
       "      <td>1992</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Adventure</td>\n",
       "      <td>6.2</td>\n",
       "      <td>434.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>tt0105000</td>\n",
       "      <td>videoGame</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>Night Trap</td>\n",
       "      <td>0</td>\n",
       "      <td>1992</td>\n",
       "      <td>\\N</td>\n",
       "      <td>\\N</td>\n",
       "      <td>Horror</td>\n",
       "      <td>6.2</td>\n",
       "      <td>434.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      tconst  titleType                  primaryTitle  \\\n",
       "0  tt0084376  videoGame  MysteryDisc: Murder, Anyone?   \n",
       "0  tt0084376  videoGame  MysteryDisc: Murder, Anyone?   \n",
       "0  tt0084376  videoGame  MysteryDisc: Murder, Anyone?   \n",
       "2  tt0105000  videoGame                    Night Trap   \n",
       "2  tt0105000  videoGame                    Night Trap   \n",
       "\n",
       "                  originalTitle  isAdult startYear endYear runtimeMinutes  \\\n",
       "0  MysteryDisc: Murder, Anyone?        0      1982      \\N             \\N   \n",
       "0  MysteryDisc: Murder, Anyone?        0      1982      \\N             \\N   \n",
       "0  MysteryDisc: Murder, Anyone?        0      1982      \\N             \\N   \n",
       "2                    Night Trap        0      1992      \\N             \\N   \n",
       "2                    Night Trap        0      1992      \\N             \\N   \n",
       "\n",
       "      genres  averageRating  numVotes  \n",
       "0  Adventure            5.8      42.0  \n",
       "0      Crime            5.8      42.0  \n",
       "0    Mystery            5.8      42.0  \n",
       "2  Adventure            6.2     434.0  \n",
       "2     Horror            6.2     434.0  "
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#\"Expandir generos para analisis por genero unicamente\"\n",
    "df_generos = df.copy()\n",
    "df_generos[\"genres\"] = df_generos[\"genres\"].str.split(\",\")\n",
    "df_generos = df_generos.explode([\"genres\"])\n",
    "\n",
    "df_generos.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Promedio</th>\n",
       "      <th>Cantidad</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>genres</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Drama</th>\n",
       "      <td>7.487977</td>\n",
       "      <td>865</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mystery</th>\n",
       "      <td>7.141818</td>\n",
       "      <td>880</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Crime</th>\n",
       "      <td>7.073082</td>\n",
       "      <td>795</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adventure</th>\n",
       "      <td>6.952898</td>\n",
       "      <td>8953</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Comedy</th>\n",
       "      <td>6.952746</td>\n",
       "      <td>1657</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Promedio  Cantidad\n",
       "genres                       \n",
       "Drama      7.487977       865\n",
       "Mystery    7.141818       880\n",
       "Crime      7.073082       795\n",
       "Adventure  6.952898      8953\n",
       "Comedy     6.952746      1657"
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings_generos = df_generos.groupby(\"genres\").agg(Promedio = (\"averageRating\", \"mean\"), Cantidad = (\"averageRating\", \"count\")).sort_values(by = \"Promedio\", ascending = False)\n",
    "\n",
    "ratings_generos = ratings_generos[ratings_generos[\"Cantidad\"] > 50]\n",
    "\n",
    "ratings_generos.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAH1CAYAAAAK4N+MAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjEsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvc2/+5QAAAAlwSFlzAAAPYQAAD2EBqD+naQAAWptJREFUeJzt3Qm8TdX///GPeSpjxjKUJkQZqq8ozRpFfSklFM0D+mqggfKNJmlQGlGppJLmSaWSFFHha5apUN/MKcT+P97r/13nt+9xLy73nrPP9no+Hqfcfc+9d+9zzl77sz7rs9YuEARBYAAAADFRMN07AAAAkJcIbgAAQKwQ3AAAgFghuAEAALFCcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAACBWCG4AOH379rUCBQqkezcAYLcR3AARNXz4cBds+EfhwoVt3333tc6dO9vPP/+8S79zw4YNLogZN25cnu8vAERF4XTvAIDtu+uuu2z//fe3v/76yyZOnOiCnvHjx9v06dOtePHiuQ5u7rzzTvfv448/Psv3brvtNrvlllvydN8BIB0IboCIO/30061Jkybu3127drV99tnH7r33XnvrrbesXbt2efZ3lBnSY0/2xx9/WKlSpSxuFNSWLFky3bsBpAzDUkCGOfbYY93/58+fn9i2adMmu+OOO6xx48ZWpkwZd4HW8z777LPEcxYuXGgVK1Z0/1b2xg93aZgqp5obfX3ttdfamDFj7LDDDrNixYpZvXr17IMPPthmvzTUpSBM2aTatWvbk08+me3v/Pjjj6158+ZWtmxZ22uvveyQQw6x3r177/C4/b68+OKL7mf0d3S8X3zxxTbPnTp1qgsKS5cu7f7GSSed5LJe2Q37ff7553b11VdbpUqVbL/99tvuPixatMhatWrlXl89v0ePHvbhhx+635M81PfNN9/Yaaed5t4PBRYtWrSwr776Kstz/Oszb948N9yo10TPv+SSS1xAkmzEiBHumEuUKGHly5e3Cy64wJYsWZLlOcrI6b367rvv7LjjjnN/27++v/76q3Xp0sUqV67sXr/DDz/cnnvuuR2+9kCm2bO7aUAGUpAi5cqVS2xbu3atPfPMM9a+fXu77LLLbN26dfbss89ay5Yt7dtvv7UjjjjCBTZDhgyxq666ytq0aWPnnnuu+9kGDRps9+9pCGz06NEuANh7773tkUcesfPOO88WL15sFSpUSAQTupBXrVrVBU5btmxxw2k+mPJmzJhhZ511lvub+r6CJV3Yky/6OVEg8sorr9j111/vfvbxxx93f1fHqAu6/xsK7BTY3HTTTVakSBEXaOmir58/+uijs/xOHZf2U8GhMjc50fdOPPFEW7ZsmXXr1s2qVKliL730UpYA0vv0009dcKVApE+fPlawYEEbNmyY+/kvv/zSjjrqqCzPVwZOQ48DBgywKVOmuPdSwZMydN7dd99tt99+u3uuMni//fabPfrooy6A0euvwMj7/fff3d9X8NOhQwcXzPz555/uNdDrrSBRf+/VV191QdXq1avdMQGxEQCIpGHDhgU6RceOHRv89ttvwZIlS4LXXnstqFixYlCsWDH3tff3338HGzduzPLzq1atCipXrhxceumliW36Pfqdffr02ebvaVtyk6CvixYtGsybNy+x7YcffnDbH3300cS2s88+OyhZsmTw888/J7bNnTs3KFy4cJbfOWjQIPe19iO39HN6TJ48ObFt0aJFQfHixYM2bdoktrVu3drt8/z58xPbfvnll2DvvfcOjjvuuG1e3+bNm7vXb0cGDhzonj9mzJjEtj///DM49NBD3fbPPvvMbdu6dWtw0EEHBS1btnT/9jZs2BDsv//+wSmnnLLNax5+j0THU6FChcTXCxcuDAoVKhTcfffdWZ43bdo09xqHt7do0cL9zieeeCLLcx966CG3fcSIEYltmzZtCpo2bRrstddewdq1a3f4GgCZgmEpIOJOPvlkl1moXr26/fOf/3RDIqq3CQ+hFCpUyIoWLer+vXXrVlu5cqX9/fffbphImYDd/fsaZvKUdVFWZMGCBe5rZWnGjh1rrVu3tmrVqiWed+CBB7rsQZjPLrz55ptuP3OradOmLhvi1ahRw8455xw3NKT90OOjjz5y+3LAAQcknqeM0oUXXuiyUMpyhSnTpddvRzQUp9lqGpbyNLSjnw/7/vvvbe7cue7vKYPy3//+1z2U+dHwmIbRko/9yiuvzPK1Mk/6Wb+vypzpZ5S18b9PD2WPDjrooG2yR8pqaWgr7L333nPPV3bPU1ZLWbD169e7rBYQFwxLARH32GOP2cEHH2xr1qyxoUOHuoujLl7JVDsxcOBAmzVrlm3evDmxXcMPu0MBRDINia1atSpRx6EhDwUzyZK3nX/+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AwAAYoXgBgAAxArBDQAAiBWCGwAAECsENwAAIFYIbgAAQKwQ3AAAgFghuAEAALFCcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAACBWCG4AAECsENwAAIBYIbgBAACxQnADAABiheAGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCmc7h1A6tS65d18/xsL7zkz3/8GAADbQ+YGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCG4AQAAsUJwAwAAYoVF/JBxWIwQALA9ZG4AAECsENwAAIBYIbgBAACxQnADAABiJa3BTa1ataxAgQLbPK655pocf+bVV1+1Qw891IoXL27169e39957L6X7DAAAoi2twc2kSZNs2bJlicfHH3/strdt2zbb50+YMMHat29vXbp0salTp1rr1q3dY/r06SnecwAAEFVpDW4qVqxoVapUSTzeeecdq127trVo0SLb5z/88MN22mmn2Y033mh16tSxfv36WaNGjWzw4MEp33cAABBNkam52bRpk40YMcIuvfRSNzSVna+//tpOPvnkLNtatmzptudk48aNtnbt2iwPAAAQX5EJbsaMGWOrV6+2zp075/ic5cuXW+XKlbNs09fanpMBAwZYmTJlEo/q1avn6X4DAIBoiUxw8+yzz9rpp59u1apVy9Pf26tXL1uzZk3isWTJkjz9/QAAIFoicfuFRYsW2dixY2306NHbfZ7qclasWJFlm77W9pwUK1bMPQAAwJ4hEpmbYcOGWaVKlezMM7d/P5+mTZvaJ598kmWbZlhpOwAAQCSCm61bt7rgplOnTla4cNZEUseOHd2wktetWzf74IMPbODAgTZr1izr27evTZ482a699to07DkAAIiitA9LaThq8eLFbpZUMm0vWPD/4q9jjjnGXnrpJbvtttusd+/edtBBB7lC5MMOOyzFew3snrjc2TwuxwEgXnYpuNGsJhUAz5w5031dr149F5xoNlJunXrqqRYEQbbfGzdu3DbbtMBfTov8AUAUgzQCNCDiw1IaBtJCe4MGDbKVK1e6x4MPPui2TZkyJX/2EgAAIL8yNz169LBWrVrZ008/naiR+fvvv61r167WvXt3++KLL3L7KwEAANIX3ChzEw5s3C8pXNhuuukma9KkSd7tGQAAQCqCm9KlS7tCX92ZO0yL4+299967sg8AgN1EcTewGzU3559/vrsr9yuvvOICGj1GjhzphqV0x24AAICMytw88MAD7saWWoNGtTZSpEgRu+qqq+yee+7Jj30EAADIv+CmaNGi9vDDD7sbUs6fP99t00ypkiVL5vZXAQAARGcRPwUz9evXz9u9AQAASEVwc+6559rw4cNdMbH+vT07uvklAABA2oMbrTysOhv/bwAAgIwObnRjy+z+DQBAXmJKO2JxV3AAAICUZ24aNmyYGJbaEe4vBQDYk8Ul+1Qrg49jp4Kb1q1bJ/79119/2eOPP25169a1pk2bum0TJ060GTNm2NVXX50vOwkAAJCnwU2fPn0S/9ZKxNdff73169dvm+dotWIAAICMqrl59dVX3erEyTp06GCvv/56Xu0XAABAaoKbEiVK2FdffbXNdm0rXrz4ru0FAABAulYo7t69u7uPlAqHjzrqKLftm2++saFDh9rtt9+eV/sFAACQmuDmlltusQMOOMDdX2rEiBFuW506ddz6N+3atdu1vQAAAEjnvaUUxBDIAACA2Czit3r1anvmmWesd+/etnLlSrdNw1Q///xzXu8fAABA/mZufvzxRzv55JPdPaYWLlzopoaXL1/e3TBz8eLF9vzzz+f2VwIAAKQvc3PDDTdY586dbe7cuVlmR51xxhn2xRdf5N2eAQAApCK4mTRpkl1xxRXbbN93331t+fLlu7IPAAAA6QtuihUrZmvXrt1m+5w5c6xixYp5tV8AAACpCW5atWpld911l23evNl9rRtqqtbm5ptvtvPOO2/X9gIAACBdwc3AgQNt/fr1VqlSJfvzzz+tRYsWduCBB9ree+9td999d17tFwAAQGpmS2mW1Mcff2zjx493M6cU6DRq1MjNoAIAAMjIRfykefPm7gEAAJDxwY1mTH322Wf266+/2tatW7N878EHH8yrfQMAAMj/4KZ///5222232SGHHGKVK1d2BcVe+N8AAAAZEdzohpm6A7gW8gMAAMj42VIFCxa0Zs2a5c/eAAAApDq46dGjhz322GO7+3cBAACiMSzVs2dPO/PMM6127dpWt25dK1KkSJbv6waaAAAAGRPcXH/99W6m1AknnGAVKlSgiBgAAGR2cPPcc8/Z66+/7rI3AAAAGV9zU758eTckBQAAEIvgpm/fvtanTx/bsGFD/uwRAABAKoelHnnkEZs/f75bwK9WrVrbFBRPmTJld/YHAAAgtcFN69atd+8vAgAARCm40ZAUAABA7O4K/t1339nMmTPdv+vVq2cNGzbMy/0CAABITXCjO4FfcMEFNm7cOCtbtqzbtnr1arfuzciRI61ixYq7ticAAADpmC113XXX2bp162zGjBm2cuVK95g+fbqtXbvWLfAHAACQUZmbDz74wMaOHWt16tRJbNNtGHS/qVNPPTWv9w8AACB/Mzdbt27dZvq3aJu+BwAAkFHBzYknnmjdunWzX375JbHt559/dncLP+mkk/J6/wAAAPI3uBk8eLCrr9ECfroNgx7777+/2/boo4/m9tcBAACkt+amevXqbhVi1d3MmjXLbVP9zcknn5y3ewYAAJDfwc3mzZutRIkS9v3339spp5ziHgAAABk7LKWi4Ro1atiWLVvybAdUr9OhQwerUKGCC5zq169vkydPzvH5Wl+nQIEC2zyWL1+eZ/sEAAD2oGGpW2+91Xr37m0vvPCClS9ffrf++KpVq6xZs2ZuAcD333/fLQA4d+5cK1eu3A5/dvbs2Va6dOnE15UqVdqtfQEAAHtocKOC4nnz5lm1atWsZs2aVqpUqV2+K/i9997raniGDRuW2Kbi5J2hYMavkLw9GzdudA9Phc8AACC+0npX8Lfeestatmxpbdu2tc8//9z23Xdfu/rqq+2yyy7b4c8eccQRLmg57LDDrG/fvi4DlJ0BAwbYnXfemWf7DAAAoi2tdwVfsGCBDRkyxG644QY31DVp0iR3C4eiRYtap06dsv2ZqlWr2hNPPGFNmjRxwc0zzzxjxx9/vH3zzTfWqFGjbZ7fq1cv9/vDmRtliwAAQDzt8l3BVfTr7wqu2y80btw4179DKxorSOnfv7/7WncW132qFLzkFNwccsgh7uEdc8wxNn/+fBs0aJCrA0pWrFgx9wAAAHuGXAc3S5cutfbt29tXX32V5a7gCjJ0V/D99ttvp3+XsjAKjMK0Zs7rr7+eq3066qijbPz48bn6GQAAEE+5XqG4a9eubr0bZW38XcH1b2Vh9L3cUJ2MZj2FzZkzxxUq54bW3VGgBAAAkOvMjQp/J0yYkGVoSP/WrReOPfbYXP0u3Y9KGR8NS7Vr186+/fZbe+qpp9wjXDOjtXCef/559/VDDz3kZlTVq1fP/vrrL1dz8+mnn9pHH32U20MBAAAxtEu3X1DmJpkW9tP08Nw48sgj7Y033nABzF133eWCFgUvF110UeI5y5Yts8WLFye+3rRpk/3rX/9yAU/JkiWtQYMG7lYQWisHAAAg18HN/fffb9ddd5099thjrhjYFxfrTuEPPPBArnfgrLPOco+cDB8+PMvXN910k3sAAADkSXDTuXNn27Bhgx199NFWuPD///G///7b/fvSSy91D0/1OAAAAJEObjRsBAAAEJvgJqf1ZwAAADJyKjgAAECUEdwAAIBYIbgBAACxQnADAABiheAGAADs2bOl2rRpYwUKFNhmu7YVL17cDjzwQLvwwguz3J4BAAAgspmbMmXKuHs5TZkyxQU0ekydOtVt02J+r7zyih1++OHuruEAAACRz9xUqVLFZWYGDx5sBQv+/9hIdwTX7Rf23ntvGzlypF155ZV288032/jx4/NjnwEAAPIuc/Pss89a9+7dE4GN+yUFC7r7Telu3srkXHvttTZ9+vTc/moAAIDUBzcaepo1a9Y227VNdwYX1d5kV5cDAAAQuWGpiy++2Lp06WK9e/e2I4880m2bNGmS9e/f3zp27Oi+/vzzz61evXp5v7cAAAB5HdwMGjTIKleubPfdd5+tWLHCbdPXPXr0cHU2cuqpp9ppp52W218NAACQ+uCmUKFCduutt7rH2rVr3bbSpUtneU6NGjV2f88AAABSEdyEJQc1AAAAGVdQrKEo1d1Uq1bNChcu7DI54QcAAEBGZW46d+5sixcvtttvv92qVq3KrCgAAJDZwY0W5vvyyy/tiCOOyJ89AgAASOWwVPXq1S0Igt35mwAAANEJbh566CG75ZZbbOHChfmzRwAAAKkcljr//PNtw4YNVrt2bStZsqQVKVIky/dXrly5O/sDAACQ2uBGmRsAAIDYBDedOnXKnz0BAABIVXCjlYj9gn1+VeKcsLAfAACIfHBTrlw5W7ZsmVWqVMnKli2b7do2mkGl7f7O4AAAAJENbj799FMrX768+/dnn32W3/sEAACQv8FNixYtEv/ef//93Vo3ydkbZW6WLFmy63sCAACQjnVuFNz89ttv22zXFHB9DwAAIKOCG19bk2z9+vVWvHjxvNovAACA/J0KfsMNN7j/K7DRTTO1gJ+nIuJvvvmG+00BAIDMCW6mTp2ayNxMmzbNihYtmvie/n344Ydbz54982cvAQAA8jq48bOkLrnkEnv44YdZzwYAAMRjheJhw4blz54AAACkI7iRyZMn26hRo2zx4sW2adOmLN8bPXp0XuwXAABAamZLjRw50o455hibOXOmvfHGG7Z582abMWOGW+ivTJkyu7YXAAAA6Qpu+vfvb4MGDbK3337bFRKr/mbWrFnWrl07q1GjRl7tFwAAQGqCm/nz59uZZ57p/q3g5o8//nDTw3v06GFPPfXUru0FAABAuoIb3URz3bp17t/77ruvTZ8+3f179erVtmHDhrzaLwAAgNQUFB933HH28ccfW/369a1t27bWrVs3V2+jbSeddNKu7QUAAEC6gpvBgwfbX3/95f596623WpEiRWzChAl23nnn2W233ZZX+wUAAJCa4KZ8+fKJfxcsWNBuueWWxNd//vnnru0FAABAumpusrNx40Z78MEHuSs4AADInOBGAUyvXr2sSZMmbp2bMWPGJFYsVlCj6eGaMQUAAJARw1J33HGHPfnkk3byySe7GhsVE+s+UxMnTnRZG31dqFCh/N1bAACAvApuXn31VXv++eetVatWbvp3gwYN7O+//7YffvjBrXMDAACQUcNSS5cutcaNG7t/H3bYYVasWDE3DEVgAwAAMjK42bJli1uR2CtcuLDttdde+bVfAAAA+TssFQSBde7c2WVsRGvdXHnllVaqVKksz+Ou4AAAICMyN506dbJKlSq5O3/r0aFDB6tWrVria//IrZ9//tn9rgoVKliJEiXcyseTJ0/e7s+MGzfOGjVq5AKtAw880IYPH57rvwsAAPbwzI2mfOe1VatWWbNmzeyEE06w999/3ypWrGhz585196/KyU8//eRu3Kms0YsvvmiffPKJde3a1apWrWotW7bM830EAAAxX6E4L917771WvXr1LIHTjhYCfOKJJ9xzBg4c6L6uU6eOjR8/3q2zQ3ADAADyZIXiXfXWW2+5RQG1Ro6GvBo2bGhPP/30dn/m66+/dmvthCmo0facFh9cu3ZtlgcAAIivtAY3CxYssCFDhthBBx1kH374oV111VV2/fXX23PPPZfjzyxfvtwqV66cZZu+VtCS3b2tBgwYkKUmSJkiAAAQX2kNbrZu3eoKg/v37++yNpdffrlddtllbugpr+iWEWvWrEk8lixZkme/GwAARE9agxsVAdetWzfLNtXQLF68OMefqVKliq1YsSLLNn1dunRpN9sqmWZU6XvhBwAAiK+0BjeaKTV79uws2+bMmWM1a9bM8WeaNm3qZkiFffzxx247AABAWoMb3b5BN97UsNS8efPspZdesqeeesquueaaLMNKHTt2THytKeCq1bnpppts1qxZ9vjjj9uoUaO4IzkAAEh/cHPkkUfaG2+8YS+//LK7X1W/fv3soYcesosuuijxnGXLlmUZptI08Hfffddlaw4//HA3JfyZZ55hGjgAAEj/Ojdy1llnuUdOslt9+Pjjj7epU6fm854BAIBMlNbMDQAAQF4juAEAALFCcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAACBWCG4AAECsENwAAIBYIbgBAACxQnADAABiheAGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCG4AQAAsUJwAwAAYoXgBgAAxArBDQAAiBWCGwAAECsENwAAIFYIbgAAQKwQ3AAAgFghuAEAALFCcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAACBWCG4AAECsENwAAIBYIbgBAACxQnADAABiheAGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCG4AQAAsUJwAwAAYoXgBgAAxArBDQAAiBWCGwAAECsENwAAIFYIbgAAQKwQ3AAAgFghuAEAALFCcAMAAGIlrcFN3759rUCBAlkehx56aI7PHz58+DbPL168eEr3GQAARFvhdO9AvXr1bOzYsYmvCxfe/i6VLl3aZs+enfhaAQ4AAEBkghsFM1WqVNnp5yuYyc3zN27c6B7e2rVrc72PAAAgc6S95mbu3LlWrVo1O+CAA+yiiy6yxYsXb/f569evt5o1a1r16tXtnHPOsRkzZmz3+QMGDLAyZcokHvo5AAAQX2kNbo4++mhXR/PBBx/YkCFD7KeffrJjjz3W1q1bl+3zDznkEBs6dKi9+eabNmLECNu6dasdc8wxtnTp0hz/Rq9evWzNmjWJx5IlS/LxiAAAwB49LHX66acn/t2gQQMX7CgrM2rUKOvSpcs2z2/atKl7eAps6tSpY08++aT169cv279RrFgx9wAAAHuGtA9LhZUtW9YOPvhgmzdv3k49v0iRItawYcOdfj4AAIi/SAU3qqeZP3++Va1adaeev2XLFps2bdpOPx8AAMRfWoObnj172ueff24LFy60CRMmWJs2baxQoULWvn179/2OHTu6mhnvrrvuso8++sgWLFhgU6ZMsQ4dOtiiRYusa9euaTwKAAAQJWmtuVEhsAKZ33//3SpWrGjNmze3iRMnun+LZk4VLPh/8deqVavssssus+XLl1u5cuWscePGLiiqW7duGo8CAABESVqDm5EjR273++PGjcvy9aBBg9wDAAAgI2puAAAAdhfBDQAAiBWCGwAAECsENwAAIFYIbgAAQKwQ3AAAgFghuAEAALFCcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAACBWCG4AAECsENwAAIBYIbgBAACxQnADAABiheAGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCG4AQAAsUJwAwAAYoXgBgAAxArBDQAAiBWCGwAAECsENwAAIFYIbgAAQKwQ3AAAgFghuAEAALFCcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAACBWCG4AAECsENwAAIBYIbgBAACxQnADAABiheAGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCG4AQAAsUJwAwAAYoXgBgAAxArBDQAAiJW0Bjd9+/a1AgUKZHkceuih2/2ZV1991T2nePHiVr9+fXvvvfdStr8AACD60p65qVevni1btizxGD9+fI7PnTBhgrVv3966dOliU6dOtdatW7vH9OnTU7rPAAAgutIe3BQuXNiqVKmSeOyzzz45Pvfhhx+20047zW688UarU6eO9evXzxo1amSDBw9O6T4DAIDoKpzuHZg7d65Vq1bNDTM1bdrUBgwYYDVq1Mj2uV9//bXdcMMNWba1bNnSxowZk+Pv37hxo3t4a9ascf9fu3ZtrvZz68YNlp9yuz+7Ir+PQTiOPecYhOPYc45BOI495xiieBz+uUEQ7PjJQRq99957wahRo4Iffvgh+OCDD4KmTZsGNWrUCNauXZvt84sUKRK89NJLWbY99thjQaVKlXL8G3369NGrwIMHDx48ePCwzH8sWbJkh/FFWjM3p59+euLfDRo0sKOPPtpq1qxpo0aNcnU1eaFXr15Zsj1bt261lStXWoUKFVwBc35QdFm9enVbsmSJlS5d2jJVHI4jDscQl+OIwzEIxxEdcTiGuBzH2hQcgzI269atc6M9kR+WCitbtqwdfPDBNm/evGy/r5qcFStWZNmmr7U9J8WKFXOP5L+TCnqDM/WDGrfjiMMxxOU44nAMwnFERxyOIS7HUTqfj6FMmTKZUVActn79eps/f75VrVo12++rJueTTz7Jsu3jjz922wEAANIe3PTs2dM+//xzW7hwoZvm3aZNGytUqJCb7i0dO3Z0w0pet27d7IMPPrCBAwfarFmz3Do5kydPtmuvvTaNRwEAAKIkrcNSS5cudYHM77//bhUrVrTmzZvbxIkT3b9l8eLFVrDg/8VfxxxzjL300kt22223We/eve2ggw5yM6UOO+wwixINg/Xp02eb4bBME4fjiMMxxOU44nAMwnFERxyOIS7HUSxix1BAVcXp3gkAAIC8EqmaGwAAgN1FcAMAAGKF4AYAAMQKwQ0AAIgVghsAABArBDcAMkJ4YieTPLGr+OzsGQhugD1QpjXw2t/wveD070w5Bt3PbntfZ5Lkfc+U9yBMnx2tl9apU6d07wryEcEN8lQmNnZ74vuTfNPYqL9vfn+feuopt1BYeFvU+YVIR44caatWrcqyMGmm8fuumxtn0nsQ9tNPP9ldd91lTZo0yehAc3uC/53PUT2v/X6tWbMm3/5G5p5lMRbVD+TO8I3dkCFD7OWXX7ZMea21SvbPP/9smzdvti1btlgc+ezHl19+6W5r0r17d3vssccy5iL1559/utu0fP/995ZpZs6caXfccYd9+umn7utMvqjqrs9dunSxJ5980jKNPjuDBw+2Zs2a2VVXXWVx49uzdevWZfmcRe3zpvZmxIgR7n349ddf8+VvENxE4IO4aNEimzFjhs2ZMyfxxkftw5gbK1eudLfF+Oabb9zXUQ0W/MX+zTfftNNOO83d/qNFixbunmXJd5+PAx3r6NGjrVWrVolbm1x33XXWuXNnFzhEXYkSJdx95N5//317++23LZMccsghtt9++9mLL77ovs7k7E358uXt7LPPtilTpmRUZ0wX/Pvuu8+ef/55d4PmwoULu/chk9va7M7xd955x1q3bm0nnHCC3X///fbLL79E5jj9Z+WPP/5w2T8FyZUqVcq3P4Y02Lp1q/v/G2+8ERx++OFBtWrVgmOOOSa46qqrEs/ZsmVLkKmeeeaZYK+99goWLFgQRNmHH34YlCpVKnjggQeC5cuXB9ddd12w9957B6+//noQN3ovDjzwwOCRRx5xX//8889BuXLlgmuvvTbbz2Y6bdq0Kdvt2reuXbsGHTt2DNavXx+JfU2WfN7+/fff7v/ffPNNUKNGjeDtt98OMkVObdAHH3wQFC5cOPjiiy+CTPLdd98FF110UVC6dOng6aefjkVbG/btt98GxYsXD2699dbgn//8Z9CsWbOgdevWwcKFCyNznOPGjQtOO+20oE2bNsHixYvz7e8Q3KTR+++/7wKARx99NJg/f34wcODAoECBAsGFF16YeE4UPozbk3xx8fu7YcOG4JRTTgluvvnmROMeJdpPXUB1kbzxxhvdtt9++y2oWbNmcM011ySet3HjxiAuZsyYETRs2ND9e9GiRcG+++4bXHHFFYnvf/3110G69evXL/j1118TX/fv3z948MEHgx9//DGx7bnnngsqVqwYzJs3L3LnSPh8UOC8efPmxP4pmDz11FODW265JXL7vSPjx493bVRYu3btgiuvvNKdI1EMMv0+rVy5Mli1alXw119/ua/nzp0bXHDBBa4z+cILLySen0nvR3ZmzpwZ3H///cE999yT2KbjO+GEE4Kzzz47EgGO/rb2ab/99gv22WefYO3atW67zpO8RnCTJsoSnHnmma7hFjXo1atXD1q2bOmyOOeff37kT7rwfuk4Pv3002Dp0qWJbbfffntQv379RIAQxQbw3HPPddkzvR963S+//PLE9958883gs88+CzKVf711kX3rrbfcxemwww5z/65Vq5Y7Vt+oKHg455xzsgQRqfbll18GBx98cHDGGWcE//3vf902BcdqCI866qjg4osvDn766Se3XRcnPaL0mQqfD3PmzAlKlCgRNG/ePOjevbv7fMno0aPd9unTpwdRFn5dp06dGhQsWDBxLGqr9P0XX3zRtVm///77Nj+Tbn5f9Flv2rSpy44fdNBBwfDhw1179J///Md1IpXZ0HHEISvbokWLoEqVKq6THKZg4vjjj3cZnChk0hVsvvTSSy5r3LZt28T2vO4EE9ykkTI206ZNC1asWBHUq1fP9YKU8VAmQRkcBT9RFW7Ivv/++6BLly7uxNJJpJNLWZE///zTBTd33HFHEDX+QqTgRhmmAw44wA0J+ou9ehQKMBW0RTHzlJuAQSl4NeC//PKLCxw07KZed9hNN90UHHfccVmyJqmm1/7ll192Fxylrf1FUxkaBQW6QDVu3Ngdg4am1CPVMUXhwhr++5dddpk7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wctQFPbEc1zBjYKYiy++2A1JTZgwwT1X54gCmr59+7pHvXr10n0IezSGpYBdoBR0s2bNbPLkyW6I6ZxzzrEjjzzS2rVr575/3nnnuUzNvffeayeccIKVLVvWevXqZStXrrT77rvPypQpk+5DALAb5/gff/xhXbt2dUPOH330kXtu1IeY9yQEN8Au0tCfemoa+lNxrYZuWrZsaWeffbZLS5977rm2ePFi++9//2u1atWyiRMnuoaSoUIgc8/xM844w03UuOKKK1xhcc+ePV3B8JtvvmnHH398uncZ/0NwA+yicePGud6chp+aNGliy5Yts6eeesruvvtuO/HEE914u8bkNaNi1apVLptz8MEHp3u3AezmOa6ZUSqsv+SSS1wJwNNPP+2eM2/evIwbco4ram6AXaRemsbcH3roIfvrr7/cVE9Nz61du7bts88+rjenoSilqTWDisAGiMc5rkysJm689NJLriOz7777uswsgU10MNUB2A1HH320W9uiaNGibvxdPT314FRMqGLEDz/80KWwGYcH4nmOjx071tXV7bfffuneVYQwLAXsphYtWtj48eOtSpUq9t5779nhhx+e7l0CkIc4xzMPw1LALvL9gptvvtnNpnjsscdco0d/AYgHzvHMRXAD7CI/1NS4cWO3ltB3332XZTuAzMY5nrkYlgLywIgRI9wtCT799FO3NDuAeOEczyxkboA8oIJCLfBVrVq1dO8KgHzAOZ5ZyNwAeURTRZkKCsQX53jmILgBAACxwrAUAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAACAWCG4AQAAsUJwAwAAYoXgBkBaLF++3Lp16+ZuSKiF0SpXrmzNmjWzIUOG2IYNG9K9ewAyWOF07wCAPc+CBQtcIFO2bFnr37+/1a9f34oVK2bTpk2zp556yvbdd19r1apVWvZN65pu2bLFChemeQQyFZkbACl39dVXu+Bh8uTJ1q5dO6tTp44dcMABds4559i7775rZ599tnve6tWrrWvXrlaxYkUrXbq0nXjiifbDDz8kfk/fvn3tiCOOsBdeeMFq1aplZcqUsQsuuMDWrVuXeI7u5jxgwADbf//9rUSJEnb44Yfba6+9lvj+uHHj3F2e33//fXf3ZwVZ48ePt40bN9r1119vlSpVcpml5s2b26RJk1L8SgHYFQQ3AFLq999/t48++siuueYaK1WqVLbPUbAhbdu2tV9//dUFHt999501atTITjrpJFu5cmXiufPnz7cxY8bYO++84x6ff/653XPPPYnvK7B5/vnn7YknnrAZM2ZYjx49rEOHDu55Ybfccov7uZkzZ1qDBg3spptustdff92ee+45mzJlihs+a9myZZa/DSCidG8pAEiViRMn6n52wejRo7Nsr1ChQlCqVCn3uOmmm4Ivv/wyKF26dPDXX39leV7t2rWDJ5980v27T58+QcmSJYO1a9cmvn/jjTcGRx99tPu3flbfnzBhQpbf0aVLl6B9+/bu35999pnbnzFjxiS+v379+qBIkSLBiy++mNi2adOmoFq1asF9992Xp68HgLzHoDKASPj222/dENJFF13khoQ0/LR+/XqrUKFCluf9+eefLlvjaThq7733TnxdtWpVl+2RefPmueLkU045Jcvv2LRpkzVs2DDLtiZNmiT+rd+/efNmVxfkFSlSxI466iiX2QEQbQQ3AFJKwzsadpo9e3aW7aq5EdXFiAIbBSqqiUmmQuRw0BGm360gyf8OUR2PipTDVFsTltMQGYDMQ3ADIKWUiVEmZfDgwXbdddflGFSovkbTxVV4rOzMrqhbt64LYhYvXmwtWrTY6Z+rXbu2FS1a1L766iurWbOm26ZMjgqKu3fvvkv7AiB1CG4ApNzjjz/uhnw0FKQZTyrgLViwoAseZs2a5WYtnXzyyda0aVNr3bq13XfffXbwwQfbL7/84rIwbdq0yTKMlBMNV/Xs2dMVESuboxlPa9ascUGLZl916tQp259TwHXVVVfZjTfeaOXLl7caNWq4fdAQV5cuXfLhFQGQlwhuAKScMiNTp051a9z06tXLli5d6jIsyrQoGNFUcQ0vvffee3brrbfaJZdcYr/99ptVqVLFjjvuOLfg387q16+fm0quWVNaX0dDWsoK9e7de7s/p5lTCoguvvhiN7VcwdSHH35o5cqVy4NXAEB+KqCq4nz9CwAAACnEOjcAACBWCG4AAECsENwAAIBYIbgBAACxQnADAABiheAGAADECsENAACIFYIbAAAQKwQ3AAAgVghuAABArBDcAAAAi5P/B7fxAXTC38lQAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ratings_generos.Promedio.head(10).plot(kind = \"bar\")\n",
    "plt.xlabel(\"Genero\")\n",
    "plt.ylabel(\"Rating promedio\")\n",
    "plt.title(\"Ratings por genero\")\n",
    "plt.ylim(5,8)\n",
    "plt.xticks(rotation = 45)  \n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Los videojuegos con elementos dramáticos presentan los ratings promedio más altos. Esto sugiere que las experiencias narrativas profundas y centradas en personajes generan mayor valoración por parte de los usuarios."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Juegos por años"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "startYear\n",
       "2026      8\n",
       "2025    323\n",
       "2024    467\n",
       "2023    478\n",
       "2022    471\n",
       "Name: tconst, dtype: int64"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "juegos_por_año = df.groupby(\"startYear\")[\"tconst\"].count().sort_index(ascending = False)\n",
    "\n",
    "juegos_por_año.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjsAAAHHCAYAAABZbpmkAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjEsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvc2/+5QAAAAlwSFlzAAAPYQAAD2EBqD+naQAAc6lJREFUeJzt3Qd8U9UXB/DTvXdpoVDKpuy9ZSOIgIAoDhRUXIiDIQr+URRUHCioDBcKDhBQ9t57T9l7lFFaKN105/85J30xLelISZrk5ff9fEJekpfk5jUkJ/eec6+DRqPREAAAAIBKOVq6AQAAAADmhGAHAAAAVA3BDgAAAKgagh0AAABQNQQ7AAAAoGoIdgAAAEDVEOwAAACAqiHYAQAAAFVDsAMAAACqhmAHwEZ16NBBTkXZvHkzOTg4yLmpPPfcc1SpUqUS35/vy49R2scCLGPr1q1UpkwZatasGZ08eZJeffVVmjx5sqWbBXYEwQ5AMZw/f55eeeUVqlKlCrm7u5Ovry+1adOGvvnmG7p7967ZnvfEiRP04Ycf0qVLl8z2HADm9t1339EjjzxCderUofr169P8+fOpT58+lm4W2BFnSzcAwNqtWLGCHn/8cXJzc6OBAwdS3bp1KSMjg7Zv306jRo2i48eP048//mi2YOejjz6SXov8PSlr1641y3PaIhwL68Y/CgICAsjDw4O++uorOff09LR0s8COINgBKMTFixfpySefpIiICNq4cSOVK1dOd9vQoUPp3LlzEgxZgqurq0We1xrhWJheWlqaHFdHx/sfAAgLC9NtBwUF3ffjARgLw1gAhfjiiy8oOTmZZs6cmSfQUVSrVo3eeust3eVff/2VOnXqRCEhIdITVLt2bZoxY8Y99+Nemp49e0rvUPPmzWVojIfIfvvtN90+s2bNkh4l1rFjR8m70c+9MZSncvXqVRke8PLykjYMHz6c0tPT73n+bdu2yWNXrFhR2hkeHi77GhqSW7x4sfRmcRv5fNGiRcU+fhqNhj7++GOqUKGC/JLn18E9YYbEx8fTsGHDpC3cJj62n3/+OeXk5BT5PPmPBR87Plb5h/8Kyl/as2cPPfTQQ+Tn5yftbN++Pe3YseOe5+H7NW3aVI5F1apV6YcffpBhRn5MfVlZWTRhwgTZh18L/73fe++9e/4W+/fvp27dulFwcLD0dlSuXJleeOGFIl+v8v7hHq2GDRtKe/i9tnDhwnv2vXDhgvytAwMD5bW1bNnyngBdOS5//fUXjR07lsqXLy/7JiYmFtiGSZMmUevWrSV44bY3adKE/v7773v248d9/fXXde8jPh48nLV69ep79j106BB1795dhom9vb2pc+fOtHv37iKPB0BR0LMDUIhly5ZJEMIf6sXBgQ1/kHN+grOzs9z/tddeky9s7gnSx71Cjz32GA0ePJgGDRpEv/zyiyTt8pcGP0a7du3ozTffpG+//Va+KGvVqiX3U87z40CFvxyuXLki9+Nf07///rv0SOW3YMECSk1NpSFDhsiX1d69eyWvgoMlvk3BX6b9+vWTL9KJEyfS7du36fnnn5fgpTg++OADCXYefvhhOR08eJC6du0qw4D6uC0cYFy7dk1yozgI27lzJ40ZM4Zu3LhBU6ZMIXPh48NfsHzcx40bJz0ZStDKQSEHo8oXMQdEHPTy0GJ2djaNHz9eEm/ze/HFF2n27Nny9x05cqQEU3z8ODlXCRZjYmLkWPD9R48eTf7+/hKcGQpYDDl79iw98cQTkuzL7x9uMwc1HEQ8+OCDss/NmzflvcvHl98T/LfmdvH7kwOTvn375nlMDtC4N+ftt9+WwKywHjMemuLHGTBggPw9OVDi51++fDn16NEjz74c1PPr4v8LPj4+8p7m9xW/V5WeHg6C27ZtK4HOO++8Qy4uLhJMchC7ZcsWatGiRbGOC4BBGgAwKCEhQcP/RXr37l3s+6Smpt5zXbdu3TRVqlTJc11ERIQ89tatW3XXxcTEaNzc3DQjR47UXbdgwQLZb9OmTfc8bvv27eWkmDJliuw7f/583XUpKSmaatWq3fMYhto5ceJEjYODg+by5cu66xo2bKgpV66cJj4+Xnfd2rVr5fH4NRSGX4+rq6umR48empycHN317733ntx/0KBBuusmTJig8fLy0pw5cybPY4wePVrj5OSkuXLlSqHPlf9Y/Prrr/IcFy9ezLMfHwP9Y8Htql69uvyN9NvIx6dy5cqaBx98UHddr169NJ6enppr167prjt79qzG2dlZHlNx+PBhufziiy/mee63335brt+4caNcXrRokVzet2+fxljK++eff/7J837lv1WjRo101w0bNkz227Ztm+66pKQkeW2VKlXSZGdn5zku/D419N4wJP9+GRkZmrp162o6deqU53p+XH4fnDt3TnfdkSNH5PrvvvtOd12fPn1kv/Pnz+uuu379usbHx0fTrl27Yh4ZAMMwjAVQAKULn3+JFhd35ysSEhLo1q1b0mPBQwl8WR/3lvAvWQX/wq9Zs6bsWxIrV66UXgfuTVDwUMTLL79caDtTUlKkndwDwN9N3IPBuEfl8OHD0mvAwzsK7jXgthdl/fr18ov/jTfeyDPMw0NV+XFvEh8LTmLltiinLl26SA8Kly6bA78+7iF5+umnpddKeV4+JtxLxs/LvXLcBn49PESon3/CQ23cK5T/78BGjBiR53ru4WHKEBL35DDuCcnMzDS67dwO/Z4Z7hHhBHr++0VHR+vawj1TDzzwgG4/Hh7i9wT3InECvD7+W+u/Nwqjv9+dO3fk/c1/Q+69y4//jjykp+CKLG6v8l7n48u9iHx8uSdVwe9n/ttwz1BhQ2oARcEwFkAB+MOYJSUlFfs+nOfBQyG7du2SoQN9/GWgHzTwUE1+/GXPXxwlcfnyZfnyzZ8/wgFUfjx8wENMS5cuvef5lKCMH49Vr179nvvzYxr6UsvfHkP356COX6c+Djj+/fdfg0NCypCPOfDzKl/yBeHjwcm6PEzIxze//Nfx6+ahsPzXly1bVgIc5bhwEMxDOTwkxnPO8HANf9nzlzvntRTF0N+6Ro0acs6BDD8fP5eh4R9lKJRv5zwaBecMFRcHaTxEyQGjfi5S/jYV570eGxsr/18MvVe5rRxwRkVFyfAuQEkg2AEoJNjhX8/Hjh0r9lw83BsQGRlJX3/9tSTacs4D/7rmL7P8ibZOTk4GH0fb828+/Cuae2fi4uLo3XfflfZyQjPny3DOUHESgk2Nn5PbxLkahihf4sVl6AtXee35n5d9+eWXkuhrCPeEcLBjrILaoH87581wAi7ndq1Zs0aSk7k0m6/j5y1txe3V4VwmztfhvLLp06dLDwzn2HDe0Jw5c+7Z31LvdQAFgh2AQnDFC8+hwz01rVq1KnRf/sLiX7jcW6L/S3bTpk0lfv6ivjD1cXk8B2b8BaJ/v9OnT+fZ7+jRo3TmzBlJVOVhD8W6devueTz93g99+R+zoPYo99cfmuBf8fl7k3iIg6veeLjDFJSeI67w0qf0qug/rxLYFvbcXNnGFU+cVJ5f/uv4dXMQxa9bP5mck4W5PcpxUXB1FJ8++eQTCRQ44ZeTfTnJuTD8vPn/1vx3ZcqcTPxchv5Wp06d0t1eEv/8848cDw7Q9HuhONgpCe7R4yHXgtrKPWX84wGgpJCzA1AI7mngXg/+4uEvK0O9OVyVov/rVf/XKg+BlPQLgPFzG/rSNoSrna5fv56n/JeHBvJPeGionbytvA4F/1rn3g4OivTzjTgoyp/rYQgHD/xrn6u89J/LUGVV//79JaDkL8/8+LVzKbcxlCBGP9eHe3XyHwuuwOJ9uYyag638ODBTjhm/Hi6f5mOsH3CsWrXqnr+DodfJvX1MqVTigC9/z4bSu2RouoD8uB360wBwTgtPXcCPwUNYSlu40o6PrYLzkfg4cEBUnNwrQ/h4cJCl31PGQ2d8fEr6eFyZtmTJkjzTBfD/OQ4AOedIGVYGKAn07AAUgr8I+cOWS3z5V7r+DMpcGs2JtcoaT/xhzcNWvXr1kvJp/vL86aefpFeAk31Lgr+4+IuA55vhgIN/RSvz+OT30ksv0dSpU6WNBw4ckGCFS8/zz1TLw1b8uri8mIeu+EuEf6kbyhXicmn+cuYvGx5i4aEvDl44d8JQcJD/1zo/Bz8G95DxFy8nz3JwwPPK6OOZqLlHjPdTyu/5S5l7oTh44y/A/PcpDLePe0u4dJ3bzHPMcG9J/qCJewx+/vlnSTLm+3BZPc8xw8eFe+T42HCPHeP5dDiJlpcJ4ZJ9/qLn483vB85bUTRo0EBygDig4ECNc3M44OCgkXNyeK4hxpd5CIiTjPnvwblh/H7h51QCpsLw0B5PW7Bv3z4KDQ2VqQs4ONAPrrmkfe7cufL6uPScjwM/L0+WyX/zkk4YyO8JDt64FJ9zjDinatq0aZJHxLlXJcH5PxxI83uNS9R56gYuPefAj+e7ArgvBVRpAYAeLol+6aWXpFyXy2O5HLZNmzZSOpuWlqbbb+nSpZr69etr3N3dZd/PP/9c88svv9xTBs2lw1ySXVQJNfvpp5+kJJhLsPXLpg3ty2XjjzzyiJRIBwcHa9566y3N6tWr7yk9P3HihKZLly4ab29v2Y9fm1IOzGXb+ri8uVatWlIWX7t2bc3ChQulbLyo0nPGpc0fffSRlER7eHhoOnTooDl27JjcV7/0XCmJHjNmjJTK8zHmdrVu3VozadIkKWsujKFjwSXM/Bq53aGhoVLyvm7dOoOl/IcOHdI8+uijmqCgINmf29e/f3/Nhg0b8uzHl7m0m9tXtWpVzc8//yxTBfDfW19mZqa8bi7xdnFx0YSHh8tr03+vHDx4UPPUU09pKlasKM8ZEhKi6dmzp2b//v1FHlfl/bNmzRp5v/H9IyMjZaqC/Pg4PPbYYxp/f39pZ/PmzTXLly/Ps49Sem7o/gWZOXOmlO0rz83vm3HjxuUpw2d8eejQoQZfQ/73AB8TngaA35f8Hu7YsaNm586dxW4TQEEc+J/7C5cAACyLS56514vLw0sb99bwhHiGcpvMhYeguEeJK6IAoGjI2QEAm8fDhMYMc5VU/uU0OMDharv8y3YAgHVBzg4A2CzOm+JlCDhRnMvozY2ryjiniM+5souXB+E8rYJK5gHAOiDYAQCbxQm9nPDMszJzcrG5cUIuJ/zyDMU8bMbTEXz66acGJ14EAOuBnB0AAABQNeTsAAAAgKoh2AEAAABVQ85O7vo4PBspr25tzPT8AAAAYDmcicMTcvI6hoVNkolgJ3faday7AgAAYJuioqKoQoUKBd6OYIdIenSUg4X1VwAAAGwDrwnHnRXK93hBEOzorSzNgQ6CHQAAANtSVAoKEpQBAABA1RDsAAAAgKoh2AEAAABVQ7ADAAAAqoZgBwAAAFQNwQ4AAACoGoIdAAAAUDUEOwAAAKBqCHYAAABA1RDsAAAAgKoh2AEAAABVQ7ADAAAAqoZgBwAAwAplZedQela2pZuhChYPdq5du0bPPPMMBQUFkYeHB9WrV4/279+vu12j0dAHH3xA5cqVk9u7dOlCZ8+ezfMYcXFxNGDAAFmx3N/fnwYPHkzJyckWeDUAAAB5A5aZ2y/S+VjjvpMys3Oo6+St1GnSFrpyO9Vs7bMXFg127ty5Q23atCEXFxdatWoVnThxgr766isKCAjQ7fPFF1/Qt99+S99//z3t2bOHvLy8qFu3bpSWlqbbhwOd48eP07p162j58uW0detWevnlly30qgAAALQWHrpGE5afoJHzjxh1v30X4+jCrRS6Fn+Xnpm5h2KS/vvOA+M5aLjrxEJGjx5NO3bsoG3bthm8nZsWFhZGI0eOpLfffluuS0hIoNDQUJo1axY9+eSTdPLkSapduzbt27ePmjZtKvusXr2aHn74Ybp69arcvyiJiYnk5+cnj829QwAAAKYw7K9DtPjwddne815nCvV1L9b9xi87Qb/suKi7HFnWh+a90or8PFzM1lZbVNzvb4v27CxdulQClMcff5xCQkKoUaNG9NNPP+luv3jxIkVHR8vQlYJfVIsWLWjXrl1ymc956EoJdBjv7+joKD1BhqSnp8sB0j8BAACYEv9g33MxTnd5/cmbxb7fhlPafcd0j6Rgbzc6FZ1EL87eR3czkMNTEhYNdi5cuEAzZsyg6tWr05o1a2jIkCH05ptv0uzZs+V2DnQY9+To48vKbXzOgZI+Z2dnCgwM1O2T38SJEyVoUk7h4eFmeoUAAGCvouLu0o2E/4af1p8oXrBzPjaFLt9OJVcnRxrQMoJ+e6E5+bg7075Ld+j1OQclnwdsKNjJycmhxo0b06effiq9Opxn89JLL0l+jjmNGTNGuryUU1RUlFmfDwAA7M/uC7flPNTXTc53nL9NKelZRd5vQ24PUIsqgeTt5ky1w3zpl+eakZuzI204FUPv/v0v5eRYLAPFJlk02OEKK8630VerVi26cuWKbJctW1bOb97MGw3zZeU2Po+Jiclze1ZWllRoKfvk5+bmJmN7+icAAABT2n1RG+w81qQCRQR5UkZWDm07G1vk/Tac1H6ndan136hGs0qBNOOZxuTk6CBJzx+vOCnDXWADwQ5XYp0+fTrPdWfOnKGIiAjZrly5sgQsGzZs0N3O+TWci9OqVSu5zOfx8fF04MAB3T4bN26UXiPO7QEAALCEPRe0+TotqwTpApe1RQxlxadm0P7L2vt1isybotEpMpS+fKy+bHPy8vTN583UcvWxaLAzfPhw2r17twxjnTt3jubMmUM//vgjDR06VG53cHCgYcOG0ccffyzJzEePHqWBAwdKhVWfPn10PUEPPfSQDH/t3btXqrtef/11qdQqTiUWAACAqUXFpUrZuLOjAzWJCKAHa2uDnU2nYmTunYJsPh1LPEJVM9SHwgM977n90cYV6P2e2hGRL9ecNnr+Hntl0WCnWbNmtGjRIpo7dy7VrVuXJkyYQFOmTJF5cxTvvPMOvfHGG5LPw/vzZIFcWu7u/l/53p9//kmRkZHUuXNnKTl/4IEHJGgCAACwZL5O/Qp+5OnqTE0jAsjf04XupGbSgct3CryfUrHVuVbeXh19gx+oTM0rBcp2YY8F/3EmC+vZs6ecCsK9O+PHj5dTQbjyinuFAAAArIFSct6iSpCcOzs5UqeaIZJvwwGNcr0+rrLackab09NZL1/HkHoV/GjvpTg6cR1Tp9jEchEAAABq7dnhfB1Fl9yhrHUnbhpMLt53KY6S0rIo0MuVGob7F/r4dcK0hTXHriWYuOXqhGAHAADAhDhX5+qdu1I5xfk6inY1ysjcOZdupxrMtVGqsDrWDJH7FqZOmJ+cn7yRiDL0YkCwAwAAYEJ7cnt16pb3k3lyFLzdqmqQwaosmTU5N1+nSyH5OoqqZbxk3p2UjGy6dDvFxK9AfRDsAAAAmGUIS5tErE+pyso/mzLPmsw9Pi5ODtS2Rpkin4NzgCLLaYeyjiNvp0gIdgAAAMyQnNyy8r1JyMp8O4ei4ik2KV13/cbctbA4x0e/N6hYeTvXkbdTFAQ7AAAAJnIj4a6sa8UpN00r/Zevoyjr5y7l6JyfrAxbsfW5+Tqd800kWJxgBxVZRUOwAwAAYOJZkzlfx8fdxeA+D+b27ihz6vCsycp8OUWVnOurm5ukzMNYWDqicAh2AAAATJyv06Lyvfk6+UvQt529RakZWTJrcnaOpsBZkwtSs6yPVG3FpWRQdOJ/q6vDvRDsAAAAmDpfx8CkgYrIsj5UIcCD0rNyaPvZW7KSOetUjCosfe4uTlStjLdsH7+GoazCINgBAAAwgZuJaXTxVgo5SL5OYKErAyiJyquPRdPm08oq58YFOwxJysWDYAcAAMCEQ1gcgPh5GM7XUXTNHcpafPia3qzJ9yY0F6VO+f/ydqBgCHYAAABMYHducnILAyXn+TWrHEi+7s6ywnlxZ002BBVZxYNgBwAAwAT2XCw6OVnh4uRIHfXKzAtb5bwwtXODHV6i4k5KRokewx4g2AEAALhPMUlpdCFWm6/TvBjBDlPydmTW5OrBJXpeX3cXqphbwYWhrIIh2AEAADDR/DqRZX3J39O1WPfhpSN6NQijt7vWLHBOnuKoW15ZNgJJygUp3pzUAAAAUOQQlqH1sAorHf/uqUb3/dy8AvrKo9Ho2SkEenYAAABKMTnZ1JS8HfTsFAzBDgAAwH24lZxO52KSZbu4+TqmpFRkXbiVQinpWaX+/LYAwQ4AAMB92HomVjczMs+XU9pCfNwpxMdNFhc9FY2hLEMQ7AAAAJTQX3uv0OiFR2W7XY0yFmuH0ruDvB3DEOwAAAAYKS0zm975+4gEOhlZObLUwxudqlmsPZykzLBGlmGoxgIAADDCldupNOTPA9KLwpMej+xak4a0r0qOJZgB2VSwRlbhEOwAAAAU08ZTN2nYX4cpMXc9q2+fbEQPlHBCQHP07Jy5mSQ9Ta7OGLjRh2AHAACgCNk5Gvpm/Rn6duM5udww3J+mD2hMYf4eZA3CAz3Ix91ZFhU9G5OkC35AC6EfAABAEb7beFYX6AxsFUHzX2llNYEOc3BwQJJyIRDsAAAAFGH9yZtyPqZ7JI3vXdcqh4n+S1JG3k5+1vfXAgAAsCKcA3M6Okm2H65XjqwVenYKhmAHAACgEJz0m5mtIT8PF6oQYD1DV/nVLa/t2Tl5I5FycjSWbo5VQbADAABQCGXNKV5dnHNjrFWVYC9yc3aklIxsunQ7xdLNsSoIdgAAAApxLHeivrpWXuHk7ORIkeUwlGUIgh0AAIBCKBP11ckdJrJmmFzQMAQ7AAAABcjKzpEcGFY3N5CwZkrv0wn07OSBYAcAAKAAF26lUFpmDnm5OlGlIC+ydvoVWRpeBh0Egh0AAIACHMuds4bnsLHk2lfFVbOsDzk5OlBcSgZFJ6ZZujlWA8EOAABAEcnJdcpb/xAWc3dxomplvGX76FXk7SgQ7AAAABRASfS19kosfQ3CtW09cOWOpZtiNRDsAACAOHTlDsUkYehDwRPzKYm+yoR9tqBZpUA533cxztJNsRoIdgAAgI5ExVPf6TvpsRm7KC0z29LNsQqX41IpOT1LJuqrWsb6k5MVzStrg52j1xLwt8yFYAcAAGjJ4etyfiUulX7cesHSzbGq5ORa5Xxlwj5bUTHQk0J83GSJi0NX4i3dHKtgO389AAAwCy5RXnM8Wnd5+uZzdC3+Ltk7Xb6OjSQnK3hJi2a5vTv7LmEoiyHYAQCwc1xxxMGNh4sTNYkIkHllPl15kuzdcRtZJsKQ5kreDoIdgWAHAMDOrTp2Q847RpahCb3rEk8ns+LfG7Tr/G2y596u/3p2bDDYye3ZOXj5jswCbe8Q7AAA2DH+Ul99TDuE1a1OWaod5ktPt6golz9adlx1X5ST1pymsYuPUnZO4bMLc09XfGomuTg5UPVQ7bw1tqRmqA/5ujvLCugncpe7sGcIdgAA7NjZmGRZEsHVyZE6RYbIdSMfrEl+Hi50KjqJ5uy9Qmqx+XQMTd10jv7YfYW2nY0t1mSCNUJ9yM3ZiWwNz/bcNHcoay9K0BHsAADYM6VX54HqweTj7iLbAV6u9HbXGrL91dozsvSAreMeqk9W/JeHNG9fVKH7H7fByQQLnG/nEoIdiwY7H374oWSN658iIyN1t6elpdHQoUMpKCiIvL29qV+/fnTz5s08j3HlyhXq0aMHeXp6UkhICI0aNYqysrIs8GoAAGzPqtxg56G6ZfNc/1TzihRZ1ocS7mbSV2tPk62btz9KerF4QU+27sRNupWcXmTZua1VYulrXjlAzvddumP3i4JavGenTp06dOPGDd1p+/btutuGDx9Oy5YtowULFtCWLVvo+vXr9Oijj+puz87OlkAnIyODdu7cSbNnz6ZZs2bRBx98YKFXAwBgOy7fTqGTNxJl4cgHa4XmuY3nlfnwkTqyPXfvFV1Phy1KSsukyevOyPaobjWpYbg/ZeVoaOHBqwXe51juzMm1bbhnp155f5kQMS4lg87HJpM9s3iw4+zsTGXLltWdgoOD5fqEhASaOXMmff3119SpUydq0qQJ/frrrxLU7N69W/ZZu3YtnThxgv744w9q2LAhde/enSZMmEDTpk2TAAgAAIoewmpZJVCGrvJrWSWIetYvR5zL+9HSEzbbOzBj83m6lZxBVYK9aEDLCHqyWbhc/9e+KIOvKSYxjWKT0qUqrVY5H7JVrs6OEtixvRfte50siwc7Z8+epbCwMKpSpQoNGDBAhqXYgQMHKDMzk7p06aLbl4e4KlasSLt27ZLLfF6vXj0KDf3vF0m3bt0oMTGRjh8/XuBzpqenyz76JwAAe7M6dyLBh+rkHcLS997DtcjdxZH2XoqjZf9qS9RtydU7qfTz9ouyPbp7JLk4OVLPBmHk6epEF2JTaP/le4MApeS8ahlv8nR1JlumlKDvs/O8HYsGOy1atJBhp9WrV9OMGTPo4sWL1LZtW0pKSqLo6GhydXUlf39tVKrgwIZvY3yuH+gotyu3FWTixInk5+enO4WHa6N8AABbcOZmEn297oxUFGVklaw0/EbCXVlKwMFBW3JekDB/DxraoZpsf7bypCyOaUu+XHNajhH3Xj1YW/v94O3mTL3qh8n2X3ujCp5M0Abn1ykoSXmvnVdkWTRk5WEnRf369SX4iYiIoPnz55OHh4fZnnfMmDE0YsQI3WXu2UHAAwC2YuT8I7LII/Nxc6YOkSHUtXYodahZRldRVZS1x7XFHo0rBlCIr3uh+77UrgrN2HKeriek0ZmYJIosaxtJu4ej4mXNLw7oxvaoLUUwiv7NwiVpecXR6zTukdrkq3fclJ6dOmG28ToL0zgiQIbjeN6g6/F3JXi1RxYfxtLHvTg1atSgc+fOSf4O593Ex+ddxIyrsfg2xuf5q7OUy8o+hri5uZGvr2+eEwCALeCEYg50nB0dKNjbjZLSs2jZkev0xtxD1HjCOnp25h76Y/flIle7VmZN7p6vCssQdxcnCYrYPhvpIeBcnI+Xn5DtRxtVuKeXpnFFf6oe4i1LYyzNXQQ1/xw7aujZ4V6surmvw56Hsqwq2ElOTqbz589TuXLlJCHZxcWFNmzYoLv99OnTktPTqlUrucznR48epZiYGN0+69atk+Cldu3aFnkNAADmtGC/toKIh2T2vteZFr7Wml5tX5WqlvGSVa63nb1FYxcfo+d/3Ud3MwwHPLeT03XDGoUNYRkcDrl0x2aSrzkfh/ONuAIrP+7leSI3UVl/zp07KRm6RVB5Nmk1aIahLMsGO2+//baUlF+6dEmqrPr27UtOTk701FNPSS7N4MGDZbhp06ZNkrD8/PPPS4DTsmVLuX/Xrl0lqHn22WfpyJEjtGbNGho7dqzMzcO9NwAAasK5J4sPX5Ptx5tWkFlyuceFE283jOxAG0a2p3cfipRf87su3KbBsw0HPDzHDKfe8Bwy4YGexXruZsqcLRfjrL4qKz0rmz5bfUq2X25Xlcr6GR6me7RxBVkOgnvKlHl1jueWnFcK8swztGXLmmFyQcsGO1evXpXApmbNmtS/f3+ZPJDLysuUKSO3T548mXr27CmTCbZr106GphYuXKi7PwdGy5cvl3MOgp555hkaOHAgjR8/3oKvCgDAPDaeipE5U0J83Khdde3npD6uHhrSoSrNfqGZTJ638/xteum3/fcMaRWnCiu/RuEBEhhEJ6ZRVJy258Na/b7rMl2+nUplfNzolXZVCtwv0MuVuuYeg/n7o/Lm66hgCEvRrJI2UD1zM1l6ruyRRYOdv/76SyYK5FJwDnz4ctWqVXW3u7u7y5w5cXFxlJKSIoFO/lwcTmheuXIlpaamUmxsLE2aNEnm7gEAUJu/D2i/kPs2Li+T/hWkSUQgzXqhuZRXbz93K0/AwzMi7zh3S7Yfqluu2M/t4eqky/3gMnRrnkDw2w1nZXtU15rk5Vb494Ey586iQ9fkGOlmTrbhyQTzC/J2k2FOZqjU3h5YVc4OAAAYFpOURptOaxevfLxJeLGGLmY9rw14OI/nld8PyJf5plMxkttTLcRbTsZorgyHWHHuBy9/kZiWJRMI9mtSocj921QNpvL+HpSUliVJ28owli0vE1HYfDt7L94me4RgBwDABiw+dI2yczTUqKJ/sYMU/oL75blm5OHiRFvOxNKrfxygpUeuF7sKyxZzP5bk5jRxoMPLYBSF856UROWZ2y/SxVspsl1HRT07tphgbmoIdgAArBwnBCtVWMXp1cm/5MPM55pKVdLm07GS92NMFZa+prm5HxdupchyCtYmOiFN8pTYIw20kwYWx2NNKshcNErJOff0cD6PGoOd49cSKDXD/hbLRrADAGDljlxNkBW7OWDp2aD4eTaK1lWD6ZdBzWRRSBYe6FGiCfP8PV2pZqh2raj9JurdMWVl19Ij14gfjhNyi1tlxniivfY1/kv4VsNkgvlVCPCgcn7usgAqz5xdEGuvtCspBDsAAFZuQW6lEFdPlbQcunW1YBnS4kRVXv5BfzZhYygl6KZIUv5zz2WqO26NDNGZwuJD2iG6Po3KG33fJ5pV1G2rYTLB/BwcHPTyduIMzr304dLjVGfcGhqz8N8SL0NirRDsAABYMU4qVvJsHm96f8vatKkWLPPxPNn8vy92YzWvHGSSvB0eSvlq7RlKycimUX8foV25w08ldTo6iU7cSJTy+B71jO/96lwrRGakZvUrqC/YKSjniudhmrrxLLX/cjPN2nmJUjOyae7eKJmJOz5VPWXqCHYAAKzYmuPRUinEeSStqmgDDUtSKrJOXE+UMu+S4gU4ec4gxtVhr/y+n87FJJf48ZTJFjvUDJHhNmPxaug/PNuYxvaolWdIS02a5/bs8DAWB9F/7b1C7b/cRJPWnqHk9CwZvuPXz5NS7rkYR49O30mXchO2bR2CHQAAK/b3gau66iKuHLI0no2Yc354BuaDheR+FDXD8Y9bL8j2uF61ZZ0qLhd/ftZeGU4xFq/Erqxv1bcEQ1j68xO92LZKiYf4rF21Mt7k7+lCdzOzqeOkzTR64VGKSUqXfJ4pTzSkZa8/IK//7yGtJLjmRPS+03dYdfVdcSHYAQCwUrxGE08KyB4vxpwxpT4cUsL5dhYdvCYzMYf6utHTLSrSTwObUsVAT5mZ2dCMz0XhL2M+VrwCfKfIkBK1yR44OjpQ0wjt3+5GQpoEPu/3rC3LjHCekxJM86r2i4a2pgYV/OhOaiYN+GmPyfKqLAXBDgCAlfrnwFWpLmpZJdCo6qLSGsoqSZJyVnYOzdhyXrZfaluF3JydZIZfTp72dXeW3qKRC45Ib42xQ1jd65WVFdqhYIMfqCyrvfOyIltGdZTL/DfIL8THnf56uZXMx5SRnUPD5h2myevO2Gy1FoIdAAArxF/2yhCWsXPrmFuz3NyPw1HxMiRljJXHomXdqgBPF3pKL1GaJ0r84dmmkmC84t8bNGnt6WI9Hj8/78/6NCz5EJa9aFU1iNaN0C4Y6+fhUuQSIdOebkyvttcu4/TNhrP05Zri/V2sDYIdAAArxL0mV+JSJVmUeyysCS/FEOztKuXJ/17VriVVHNwrMH3TOdl+vk3le9at4i/iiY/Wl+3pm8/TvH1XinzMTadiJd+nrK87tbCCBG61cXR0oNHdIyVxmS3JzY2yi2Bny5Yt1KtXL6pWrZqcHnnkEdq2bZvpWwcAYIe4Sun73KEeLqP2dLWuxY05gVfJ/TA0Z0tBNpyMoVPRSRLADWpVqcDZjN/sVE22/7foGG0+rZ3xuSBKLknvhmHFWh4CSqZrbW3AfSs53SaHsowOdv744w/q0qULeXp60ptvviknDw8P6ty5M82ZM8c8rQQAsANX76TKxG5tPtsoSztwUdCTza1rCCv/UFZxK3X4C3Jqbq/OMy0jyM+z4CGU4Q/WkOCFZ/t9+bcDtPqYdpgqP17BXVn+ojeGsMwq2Edbzp+elSNl6rbG6J8Ln3zyCX3xxRc0fPhw3XUc8Hz99dc0YcIEevrpp03dRgAAVTsVnUg/bLkgkwfyYp/KqtvDOtegRhW1MxZbGyVJ+cClO9LmonpVdl24LTk+vGQFJ8UW1XP0xWP1KTM7h1YejabX/jxInz1an/rnLtipWHX0hiTP8hIWtcppl7EA8/B0dSZPVyeZdPB2cgb5lHAmb5sJdi5cuCBDWPnxUNZ7771nqnYBAKjesWsJ9NXa07TpdKzuujbVgmhI+2pybs3zvXBwwcNRSelZEqwVtUr49E3aYTleYbyMj3am4sJwhdB3TzUmH7ejNG9/FL3zz7+UmJYp88Dkr8Lq3SjMqo+VWgR7u0keGQ9lVQr2IlUHO+Hh4bRhwwbJ1dG3fv16uQ0AAIrGX9xP/bhbggXuFOlet5xUvdSzkaUKnJ0cqXFEAG09Eyvz7RQW7HCPDs8X5OzoQC+3+y9YKQr3Fn3Wr54MefEkhB+vOEnxqZk0smsNup6QRrsvaIfQMIRVOoK8XXXBjq0xOtgZOXKkDFsdPnyYWrduLdft2LGDZs2aRd9884052ggAoDprjkVLoBMR5Emzn29uc7+UWfNKucHOpTv0XJuCh6am5ebq8MR1FQKMmy+Ie2zGdNeWSXPZM+f9cKAY6usut7eoHCiz/YL5BeeuHRabnKH+YGfIkCFUtmxZ+uqrr2j+/PlyXa1atWjevHnUu3dvc7QRAEB1dIt7Nqlgk4GO/kzKXCbPCciGhpJ4gc51J25KsrUyX4ux+HGHdqwmAc/7S47Rb7suSy9RSVc4h/sLdm4l2UHPDuvbt6+cAADAeLFJ6bQjdxmIXg3CyFY1CPcnVydHeT08UWD+oO3A5Tv0wZJjss0z8fLEgfeDq7h8PVxoxLzDUqnFz/1wXeNXOIeSKeOtrciyi2EsRUZGBsXExFBOTk6e6ytW/G9GTAAAuNfKozdkIU0OFiKCbLNXh/HSDPUr+NH+y3ekd0cJds7HJtMXq0/RmuM35bKXqxO91bmGSZ7zkQZhsgYWL1/Ai34WVsIOphWcm1iu2mDn8uXLFBERIdtnz56lF154gXbu3JlnH6ULMzvbuKnDAQDsdQiLv7htHc+3w8EOJyl3qFmGvll/lv7aFyXl6DzSxJME8rw55fxMl1fTMTKEDr3/oFWsAm+Xw1jJKs3ZefHFFykwMFDycp577jlydnam5cuXU7ly5VDuBwBg5MSBPLzDH50969v+EAzPtzODztPq49G04ugNmYeFdY4MoXe7R1KNUPPMf4NAx5LBTjqpMtjhCQOfffZZ2eYqrAMHDlBkZKS52wYAoDrLjmhnA25ZOUhXUWTLuPycA7ekNO2sujw09173SKxTpULBSs6OWhOUH3vsMZo6daps165dm27d0ibWAQCAcZYoE+E1tP0hLMYVUi8+UFmGsl5qW0USkdHjr+6cnZSMbLqbkS2roqtqbSyeLJB7d9jnn39O77zzDm3evJlu375NiYmJeU4AAGDY2ZtJshCmi5ODTCKoFv/rUZsWvdaGHq6H1AY183FzJldnR5scyipWzw7Pjnzp0iXZ5kVAGS/8qQ8JygAAxUtMbl+jDKqIwOY4ODhQGW83uhZ/V4Kd8EDjJoi0idLzSpUqyfmmTZvM2R4AAFXiH4RKsGPLc+uAfQvyds0NdjLUPc9O+/btzdMSAAAV+/dqgky85+HiRA/WDrV0cwDsqiKrxJMKpqam0pUrV2RyQX3169c3RbsAAFRlyWFtr06X2qHk6Vrij14Aiwq20Yoso//HxcbG0vPPP0+rVq0yeDtydgAA8uIJ9pb/qw12emMIC2xYsI327BSrGkvfsGHDKD4+nvbs2UMeHh60evVqmj17NlWvXp2WLl1qnlYCANiwPRdvU0xSupRpt6tRxtLNAbC7WZSN7tnZuHEjLVmyhJo2bUqOjo6yjMSDDz5Ivr6+NHHiROrRo4d5WgoAYKOW5SYm8xw0SukugC3PtROr9p6dlJQUCgkJke2AgAAZ1mL16tWjgwcPmr6FAAA2LCMrh1YejVbNWlhg34JtdOVzo4OdmjVr0unTp2W7QYMG9MMPP9C1a9fo+++/l7WyAADgP9vOxlLC3UwK8XHDEgpg88oow1hqT1B+66236MYN7dou48aNo4ceeoj+/PNPcnV1pVmzZpmjjQAANl+F1bN+GDlh8UpQSc5OYlqW9FrayrCs0cHOM888o9tu0qQJXb58mU6dOkUVK1ak4OBgU7cPAMBmpWZk0boTN2X7EZWshQX2zc/DhZwdHSgrR0O3U9KpnJ8H2YL7Dsk8PT2pcePGCHQAAPLZeCqG7mZmU8VAT2pQwc/SzQG4b46ODjKLMruVZDsVWbbR/wQAYIOWH9EO+fesjwUyQT2CbXCuHQQ7AABmkJyeRZtOx+jydQDUIsjb9srPEewAAJjB+hM3KT0rh6oEe1Gtcj6Wbg6AXZefGxXsZGVl0fjx4+nq1avmaxEAgAooy0NgCAvUW36eQaoMdpydnenLL7+UoAcAAAzjeXW2nNFOuNoTEwmCygTbQ85Op06daMuWLeZpDQCACnC5eWa2hmqEelONUAxhgboE+6h8GIt1796dRo8eTW+//TbNnTtXFv/UP5XUZ599Jl29vNCoIi0tjYYOHUpBQUHk7e1N/fr1o5s3tXNWKK5cuSLrcXEJPC9jMWrUKPQ8AYCVDGGhVwfUJ9gGe3aMnlTwtddek/Ovv/76nts4WMnOzja6Efv27ZNlJ+rXr5/n+uHDh9OKFStowYIF5OfnR6+//jo9+uijtGPHDrmdn4sDnbJly9LOnTtlZueBAweSi4sLffrpp0a3AwDgft1JyaDtZ2/Jdo/6WEIH1Bvs3Lahlc+N7tnJyckp8FSSQCc5OZkGDBhAP/30kywsqkhISKCZM2dKUMVDZzxb86+//ipBze7du2WftWvX0okTJ+iPP/6ghg0bSq/ThAkTaNq0aZSRYTt/BABQjzXHo2V22VrlfKlqGW9LNwfAbMFOXGoGZWXnkC2weOk5D1Nx70yXLl3yXH/gwAHKzMzMc31kZKQsS7Fr1y65zOe82npoaKhun27dulFiYiIdP368wOdMT0+XffRPAACmsPzf/yYSBFCjQC9X4mXeNBptwKPaYIcTlHv16kXVqlWT0yOPPELbtm0z+nH++usvOnjwIE2cOPGe26Kjo2VxUX9//zzXc2DDtyn76Ac6yu3KbQXh5+NhMeUUHh5udNsBAPK7nZxOO89rh7AQ7IBaOTk6SMBjS+XnRgc7PGTEvS2cEPzmm2/KycPDgzp37kxz5swp9uNERUXJCuq8Yrq7uzuVpjFjxsgwmXLitgAA3K9Vx6IpR0NUr7wfRQR5Wbo5AGYTbGNJykYnKH/yySf0xRdfSPKwggMezq3hfJmnn366WI/Dw1QxMTGyiKiCc362bt1KU6dOpTVr1kjeTXx8fJ7eHa7G4oRkxud79+7N87hKtZayjyFubm5yAgAw10SCAGoWZGOzKBvds3PhwgUZwsqPh7IuXrxY7MfhnqCjR4/S4cOHdaemTZtKsrKyzVVVGzZs0N3n9OnTUmreqlUruczn/BgcNCnWrVtHvr6+VLt2bWNfGgBAicUkptGei3GyjSosULtgtffscH4LByCcq6Nv/fr1RuW++Pj4UN26dfNc5+XlJXPqKNcPHjyYRowYQYGBgRLAvPHGGxLgtGzZUm7v2rWrBDXPPvus9DZxns7YsWMl6Rk9NwBQmlYevSEJm40q+lOFAE9LNweglIKdDFJlsDNy5EgZtuLel9atW8t1PO/NrFmz6JtvvjFp4yZPnkyOjo4ymSBXUHGl1fTp03W3Ozk50fLly2nIkCESBHGwNGjQIFm/CwDAMlVYmEgQ7CjYSbKNnh0HjYZ/ixhn0aJF9NVXX9HJkyflcq1atWTm4t69e5Mt4tJzrsriZGXuQQIAMMaNhLvUauJG2d41phOV8/OwdJMAzGrB/iga9fe/1LZ6MP0+uIXVf38b3bPD+vbtKycAACBakdur06xSAAIdsAvBPrY1i3KJgh22f/9+Xc8O583wDMcAAPYIQ1hgb8qoPUH56tWr9NRTT0mejlISzuXhnL/DkwRWqFDBHO0EALBKUXGpdDgqXmaU7V6v4CkvAFS5PlZKBuXkaMiR/wOoqfT8xRdflGUcuFcnLi5OTrzNa2PxbQAA9mTTae3UF80qBVKIT+lOkApg6Xl2snM0FH83k1TXs8NLRfBinDVr1tRdx9vfffcdtW3b1tTtAwCwarvO35ZzTtQEsBcuTo7k7+lC8amZMpSlLB+hmp4dnkuHe3by49mPw8IwXg0A9oO773df0AY7raoGWbo5AKUq2IbKz40Odr788kuZ3I8TlBW8zetcTZo0ydTtAwCwWmdikuhOaiZ5uDhRvfJ5Fy0GULug3N6cWBtIUjZ6GOu5556j1NRUatGiBTk7a++elZUl2y+88IKcFJzPAwBQmmbvvETXE+7S211rSld7aQxhNa0UQK7O5n0uAGstP79lA+XnRgc7U6ZMMU9LAABMUBn14bLjsmxD4t1M+rRvPXJwcDB7sIMhLLBHZWyo/NzoYIeXYwAAsEZz916RQEe7HUWVgrzolfZVzZavoyz82aoKgh2wP8HKyudqzNkBALBGGVk5NH9/lGx3qRUq5xNXnZIFOs3hZHQiJdzNJC9XJ6pb3s8szwFgK3PtWDsEOwCgCutO3JTcgTI+bjTjmcb0XOtKcv3weYfp0JU7Rd7/bkY2nb2ZZPQQVrPKgWbPDQKw7pXP08na4X8oAKjCnL2X5fyJpuESfLzfszZ1jgyh9Kwceum3/ZLPY0hWdg7N2XOF2n+5iR6cvJUWH7pWrOfbfQFDWGDfgpUEZQxjAQCY36VbKbTj3G3iXOQnm4fLdU6ODvTtU42oTpiv9Pg8P2ufDDspNBoNrTkeTd2mbKX3Fh2lmNwP7Fk7LxX5fDxr7J6L2p6dlgh2wN5zdpIz5P+TqoMdXl598eLFukVBAQAskZjM2tcoQxUCPHXXe7k508xBzaisrzudi0mmIX8ckNyeA5fj6LHvd9Ervx+g87EpFODpQqO61ZQAide5OhdT+HDWieuJlJSWRT5uzhJMAdjzMFZGdg4lpmWRqoKd/v3709SpU2X77t271LRpU7mufv369M8//5ijjQAABUrPyqYFB67K9tPNK95ze1k/d/rluWaSSLzz/G3pyek3YxcduHyH3F0caWjHqrTlnY40tGM16lizjNxnwX7t4xVEmTW5eeVAcka+DtgpdxcnCfhtIW/H6P+lW7du1a2BtWjRIum64lXPv/32W/r444/N0UYAgAKtOX6T4lIypPemU2SIwX1qh/nS1Kcby8rkF2+lyPmTzcJp89sdaVS3SPJ1d5H9HmuiHQJbeOia5PIUZFdusIMhLLB3wTaSt2N0sJOQkECBgYGyvXr1aurXrx95enpSjx496OzZs+ZoIwBAgebs0SYm928WXmgvS8fIEJr2dGN6ukVFWjOsHX3Wr770+ujjYIkXNIxNSqctZ2INPg4HQXuV+XUwmSDYuWC9vB3VLQS6a9cuSklJkWCna9eucv2dO3fI3T3vBwcAgDmdj02Wqiilp6Yo3euVk1mVq4f6GLydl3zo07B8oUNZx68nUnJ6Fvm6O1OtcsjXAfsW5GUb5edGBzvDhg2jAQMGUIUKFWSV8w4dOuiGt+rVq2eONgIAGDR3jzYxuWPNEArz9zDJYz7etIKcbzilHR4raAireeUgSWgGsGfBPq7qDHZee+016dn55ZdfaPv27eToqH2IKlWqIGcHAEpNWmY2/X0wNzG5xb2JySXFvTV1y/tSZrbG4Jw7WA8LwNDEgiobxmJcgdW3b1/y8vLS1dZzzk6bNm1M3T4AAINWHbtB8amZFObnTh1qGk5MLqnHcxOVlSovRWZ2Du27hMkEAWxtFuUSBTu//fabDFl5eHjIicvOf//9d9O3DgCgADzrMXuyeUWTDyf1bhhGrk6OdPJGIh27lqC7/ui1BErNyCZ/TxeKLGs47wfAngSrNdj5+uuvaciQIfTwww/T/Pnz5fTQQw/Rq6++SpMnTzZPKwEA9Jy5mUT7Lt2RIOeJYiQmG8vf05UerK1dTPRvvd4dZQirReVAckS+DgCVsZGcHe1sQEb47rvvaMaMGTRw4EDddY888gjVqVOHPvzwQxo+fLip2wgAYLBXh9e+CvU1TxXoY00r0IqjN2jx4Ws05uFIcnN20k0miCEsgHw9O0kqy9m5ceMGtW7d+p7r+Tq+DQDAnHh18oVmSEzOr131MhTq6yZ5QetPxMgyE/svaVdPb1U12GzPC2CLwc7dzGxKSc9ST7BTrVo1GbrKb968eVS9enVTtQsAwKBlR67LOjwVAjwkIDEXHiLr11hbhr7gQBT9ezVePtB50sHqId5me14AW+Ll5kweLk5WP5Rl9DDWRx99RE888YTMq6NUX+3YsYM2bNhgMAgCADAVrv78bbd2VfJnWkaYPW/msSYVaPrm87T1TKwEV6xlFeTrAOSfaycq7q4EOxFBXqSKnh1eHmLPnj0UHBwsq53zibf37t0r5egAAOZy5GoCHbuWKDMd929q+sTk/KqU8aamEQGUoyH6MzdPCPk6AIaHsmKtOG/H6J4d1qRJE/rjjz9M3xoAgEL8tkvbq9OzXjkZTioNPKPy/st3KHdKMSz+CWCDS0YY3bOTmJho8JSUlEQZGdYb1QGAbeOlG5b/qy2CeLZVRKk9b4/6YbqcBP4FWw35OgAGy89vW/EsykYHO/7+/hQQEHDPia/nCQYjIiJo3LhxlJOTY54WA4Bdmr8/SiqieCmHhuH+pfa83m7O1L1eWV2+joMD8nUAbG1iQaOHsWbNmkX/+9//6LnnnqPmzZvLdZyvM3v2bBo7dizFxsbSpEmTyM3Njd577z1ztBkA7Ex2job+3HNZtge2rFTqAce7D0VK787gByqX6vMC2IJgNQY7HNR89dVX1L9/f911vXr1kuUjfvjhB6nKqlixIn3yyScIdgDAJLgaiqs9/DxcqFeDsFJ/fp648JO+9Ur9eQFsQbANBDtGD2Pt3LmTGjVqdM/1fB2vhs4eeOABunJFW7kAAGCqxOTHm1QgD1dt/gwAWIdgb2XJCBXl7ISHh9PMmTPvuZ6v49vY7du3JY8HAOB+XbmdSpvPxMr2gJall5gMAMUT7KMsGaGiYSzOx3n88cdp1apV1KxZM7lu//79dOrUKfr777/l8r59+2TiQQCA+8W5Olz23a5GGaocbJ0TlgHYswBPbc9OUnqW5Nfx7OM2H+zwop8c2HB+zpkzZ+S67t27y+SClSpVksu8KjoAwP1Ky8ymefujZPtZ9OoAWCWP3KkZlP+zvISEtSlRiypXrkyfffaZ6VsDAKCH59XhhTjL+3tQp8gQSzcHAAxwd/kvIyY1wzqDHaNzdti2bdvomWeekZXOr127Jtf9/vvvtH37dlO3DwDs2O+7L+tWN7fGrnEAIJkKQund4Z4da2R0sPPPP/9Qt27dZALBgwcPUnq6NiEpISGBPv30U3O0EQDsEK8yfiQqnlydHOmJZuZfBwsASs4zt0qSe3ZUEex8/PHH9P3339NPP/1ELi4uuut5BXQOfgAATOH3XdpenYfrldXN4wEA1sk9t2fnrpX27Bg9sHb69Glq167dPdf7+flRfHy8qdoFACp3I+EujV92gpLSsgzevvdSXKmvgwUA99uzY/j/s80FO2XLlqVz587pKq8UnK9TpUoVU7YNAFTs1x2XaNWx6EL3qV/BjxpXxJxdANbOw9W6c3aMDnZeeukleuutt+iXX36RpKTr16/LzMlvv/02vf/+++ZpJQCozsZTMXL+crsqVLuc7z238/JXraoGYeFNABvg4aKynJ3Ro0fT008/TZ07d6bk5GQZ0nrxxRfplVdeoTfeeMOox5oxYwbVr1+ffH195dSqVSuZrFCRlpZGQ4cOpaCgIPL29qZ+/frRzZs38zwGL0vRo0cP8vT0pJCQEBo1ahRlZVlnNxoAaEXFpdK5mGSpsBrasRr1aVT+nlPvhuUpxMfd0k0FACN6du6qJdjhX1m86nlcXBwdO3aMdu/eLSudT5gwwegnr1ChgszXc+DAAZmFuVOnTtS7d286fvy43D58+HBatmwZLViwgLZs2SK9SI8++qju/tnZ2RLoZGRkyJpdvEgpr8r+wQcfGN0WACj9Xp0mEQGyuCcAqCNnJ00tw1gKV1dXql279n09Oa+Wro9XSufeHg6gOBDi9bbmzJkjQRD79ddfqVatWnJ7y5Ytae3atXTixAlav349hYaGUsOGDSXoevfdd+nDDz+UNgKA9QY7mCgQQF3VWKkZKgl2OnbsWOgY+saNG0vUEO6l4R6clJQUGc7i3p7MzEzq0qWLbp/IyEiqWLGi5AhxsMPn9erVk0BHwXMA8XIV3DtkaHV2xnMDKfMDscTExBK1GQCMx9Uauy7clm0EOwDq6tm5q5aeHe490ccByeHDh2VIa9CgQUY34OjRoxLccH4O5+UsWrRIeoz4Mblnxt/fP8/+HNhER2srOPhcP9BRblduK8jEiRPpo48+MrqtAHD/dp67TRlZObIERPUQb0s3BwBMmKBsrTk7Rgc7kydPNng9DxtxwrKxatasKYENz8DMq6ZzwMT5OeY0ZswYGjFiRJ6enfBwzNAKUBo2nv5vCAuVVgAqC3YyrTPYKdHaWIbwWllcjm4s7r2pVq0aNWnSRHpcGjRoQN98843M58OJx/knKuRqLL6N8Xn+6izlsrKPIW5ubroKMOUEAOan0WhoE/J1AFTHw9XZqnN2TBbscP6Mu/v9l4nm5ORIPg0HP7wcxYYNG/LM3syl5jzsxfich8FiYrQfnmzdunUSvNxv8jQAmN6p6CS6kZAmqyTzHDoAoA4euSufW2vPjtHDWPql38ovtRs3bkjpuLGTCvJwUvfu3SXpOCkpSSqvNm/eTGvWrJHlJwYPHizDTYGBgRLA8Dw+HOBwcjLr2rWrBDXPPvssffHFF5KnM3bsWJmbh3tvAMA6q7BaVw3WVW8AgO3zzO3ZUU3ODgch+hwdHSXvZvz48RJ8GIN7ZAYOHCjBEj8uTzDIgc6DDz6oyw/ix+fJBLm3hyutpk+frru/k5MTLV++XKqvOAjy8vKSnB9uCwBYH2UIqyOGsABUxd3KJxV00HDXjJ3jBGUOtjhJGvk7AOZxJyWDmny8jnI0RDtGd5JqLABQh/UnbtKLv+2nBuH+tGRoG6v7/jZZzg4AQGG2no2VQKdmqA8CHQC1LgSaYcPDWJwzc+bMGQoODqaAgIBCy0V5rpw6derQ559/LsNSAAD6+TodIstYuikAYKZgJzUzy3aDHc6d8fHxke0pU6YUui/n1qxcuZKef/55mQUZACA7R0NbzsTKdqeayNcBUO+kgjlks8GO/szIxZklmSusuHQcAIAdunKH4lMzydfdWRb/BACVLheRYZ09O2bJ2eHZiPXnvgEA+6YMYbWrUYacnZAqCKDmGZQ1Vlj3hE8dADC7Tadzh7BQcg6g6pydHA1Repb1DWUh2AEAs7qRcJdO3kgkrmtoXwPJyQBq7tlhaVY4izKCHQAwq02ntL06DcP9KcgbM5sDqJGzkyO55g5RW+P6WCUOdniRTl6rKivLOpORAMC68nVQhQWgbu5WvD6W0cFOamqqrFnl6ekp8+nwwpyM16367LPPzNFGALBR3J2949wt2cYSEQDq5mnF62MZHezw4p1HjhyRBTv1Vznv0qULzZs3z9TtAwAbtudinPzKC/V1ozphWIoFwB6SlO9aYc+O0QuBLl68WIIaXnlcfyZl7uU5f/68qdsHAGpY+LNmSKEzrwOAepKUU9XQsxMbG0shIfd2R6ekpODDDADy2HZWm5yMKiwAO+rZyVBBsNO0aVNasWKF7rIS4Pz888/UqlUr07YOAGy65Px8bAo5OhC1rhps6eYAQCn17KSpYRjr008/leUgTpw4IZVY33zzjWzv3LmTtmzZYp5WAoDN2X5Wm5hcr4I/+Xm6WLo5AFBai4GqoWfngQceoMOHD0ugU69ePVq7dq0Ma+3atQvrYQGAzvbcKqy21dCrA2BvS0bYfM8Oq1q1Kv3000+mbw0AqEJOjkZXct4GwQ6AXfC04sVAixXsJCYmFvsBfX1RXgpg707fTKJbyRnyS69xhL+lmwMApcDd1nt2/P39i11plZ1tfS8SACyTr9OiSiC5Of+3Zg4AqL9nJzXDRoOdTZs26bYvXbpEo0ePpueee05XfcX5OrNnz6aJEyear6UAYDO25Q5hPYAhLAC74WHr1Vjt27fXbY8fP56+/vpreuqpp3TXPfLII5Ks/OOPP9KgQYPM01IAsAnpWdm09+Jt2X6gOoIdAHvhoaZqLO7F4bl28uPr9u7da6p2AYCNOnD5DqVl5lAZHzeqGepj6eYAQClR1aSC4eHhBiuxeFJBvg0A7JuSr8NDWJhVHcAOq7EyVVB6PnnyZOrXrx+tWrWKWrRoIddxj87Zs2fpn3/+MUcbAcAG59dByTmAnc6zk6GCnp2HH35YAhvO04mLi5NTr1696MyZM3IbANiv+NQMOnotQbaRnAxgXzxcna02Z6dEkwpWqFCBPvnkE9O3BgBs2s7zt0mjIaoe4k1l/dwt3RwAKEUeVlyNZXTPDgBAQbYp+TqowgKwO55qqsYCACiIskQEhrAA7I+7Fc+gjGAHAEziyu1UuhKXSs6ODtSiSpClmwMAFlsbK5usDYIdADCJbedi5bxxxQDyditROiAAqCBnJyM7h7Kyc8ialPgTKTY2lk6fPi3bNWvWpDJlypiyXQBgq/PrIF8HwK4nFVSGsnycrKc/xeiWpKSk0AsvvEBhYWHUrl07OfH24MGDKTU11TytBACrlp2jkUoshvl1AOyTm7MjKfOIWlvejtHBzogRI2jLli20dOlSio+Pl9OSJUvkupEjR5qnlQBg1Y5dS6CEu5nk4+5MDSr4Wbo5AGABDg4OVjuxoNHDWDxL8t9//00dOnTQXceTCXp4eFD//v1pxowZpm4jANjIrMmtqgSRsxV1XQNA6eIkZS49t/meHR6qCg0Nvef6kJAQDGMB2Cnk6wBAnvLzDBsPdlq1akXjxo2jtLQ03XV3796ljz76SG4DAPvCH2q80jnD/DoA9s3TVSXDWFOmTKGHHnpIloxo0KCBXHfkyBFyd3enNWvWmKONAGDF9ly8LaWm5f09qHKwl6WbAwAW5GGlEwsaHezUq1dPFgL9888/6dSpU3LdU089RQMGDJC8HQCw0yGsasGSoAgA9svDSpeMMCrYyczMpMjISFq+fDm99NJL5msVANgEjUZDG07FyDbydQDAw0p7dozK2XFxccmTqwMA9u3YtUS6eCtF5tfoGBli6eYAgIV5ujqrI0F56NCh9Pnnn1NWVpZ5WgQANmPpkWty3qVWKJaIAACy1sVAjf502rdvH23YsIHWrl0r+TteXnkTEhcuXGjK9gGAlcrJ0dDyf2/I9iMNwyzdHACwomqs1AwbD3b8/f2pX79+5mkNANiMfZfi6EZCmsya3KEm1sYDANIlKKfZes/Or7/+ap6WAIBNWXrkupw/VKcsuTn/twAgANgvj9xhrNQM60p1KdG87pyvs379evrhhx8oKSlJrrt+/TolJycb9TgTJ06kZs2akY+Pj8zA3KdPH91K6gpOiOY8oaCgIPL29pZepZs3b+bZ58qVK9SjRw/y9PSUxxk1ahRyigDMKDM7h1YexRAWABju2bmbkUM2HexcvnxZcnV69+4tQUhsbKxcz0nLb7/9tlGPxYuH8mPs3r2b1q1bJ6XtXbt2lZXVFcOHD6dly5bRggULZH8Oqh599FHd7dnZ2RLoZGRk0M6dO2n27Nk0a9Ys+uCDD4x9aQBgxNw6d1IzKdjbVdbDAgDIM4NyZpZtD2O99dZb1LRpU5k1mXtbFH379jV67p3Vq1fnucxBCvfMHDhwgNq1a0cJCQk0c+ZMmjNnDnXq1Ek3jFarVi0JkFq2bCmJ0idOnJCeJl6zq2HDhjRhwgR699136cMPPyRXV1djXyIAFHMIq2f9MCz8CQDqWxtr27ZtNHbs2HuCiEqVKtG1a9oy1JLi4IYFBgbKOQc93NvTpUsX3T48qWHFihVp165dcpnPuadJf3HSbt26UWJiIh0/ftzg86Snp8vt+icAKB7+EFt7PFq2ezXAEBYAWH81ltHBTk5Ojgwd5Xf16lXJvSkpftxhw4ZRmzZtqG7dunJddHS0BFVcAaaPAxu+Tdkn/yrsymVlH0O5Qn5+frpTeHh4idsNYG82noqhlIxsqhDgQY0r5v2/CQD2zcPFOquxjA52OKeGFwNV8Fo4nJjMK6E//PDDJW4I5+4cO3aM/vrrLzK3MWPGSC+ScoqKijL7cwKoxZLD13S9OlgLCwBUtzYW++qrr2SYqHbt2lIp9fTTT8vCoMHBwTR37twSNeL111+X9ba2bt0qq6krypYtK4nH8fHxeXp3uBqLb1P22bt3b57HU6q1lH3yc3NzkxMAGCfhbiZtPq0tSngEQ1gAoMa1sRgHI5yc/N5770mlVKNGjeizzz6jQ4cOSXKxsYsIcqCzaNEi2rhxI1WuXDnP7U2aNJH1uHjGZgWXpnOpeatWreQynx89epRiYrSLETKu7PL19ZWADABMZ83xaMrIzqEaod4UWbbkw9YAoPbS82yyJiVazMbZ2ZmeeeaZ+35yHrriSqslS5ZIvo+SY8N5NB4eHnI+ePBgGjFihCQtcwDzxhtvSIDDlVjKsBoHNc8++yx98cUX8hicQM2Pjd4bANNalluFxb06GMICgPw8XZytsmenRMEOz3Wzfft26U3hxGJ9b775ZrEfZ8aMGXLeoUOHPNdzeflzzz0n25MnTyZHR0eZTJCrqHgIbfr06bp9nZycZAhsyJAhEgTxWl2DBg2i8ePHl+SlAUABYpPSace5W7KNKiwAMMTd1VEX7PDojbX8KDI62OG5cF555RWpkuJ5dvRfCG8bE+zwgSiKu7s7TZs2TU4FiYiIoJUrVxb7eQHAeCv+vU45GqIG4f4UEZR3AWAAAObpqg0r+Os9PStHN++OzQU777//vsxOzBVN3OMCAPY1kSASkwGgqARlJW/HWoIdo6OV1NRUevLJJxHoANiRqLhUOnglnrgjt1f9cpZuDgBYKSdHB3J11sYHqVaUt2N0zw4nDPM6VaNHjzZPiwDAIn7bdYlOXE+kAC9XCvR01Z57uZC/pyutPa6dzoHXwQrxdbd0UwHAynt3MrJyrKoiy+hgh2cf7tmzp6xrxcs0cGm4vq+//tqU7QOAUnDmZhJ9sMTw8ir6MIQFAMVZMoLn5LL5YGfNmjVUs2ZNuZw/QRkAbM/Sw9p8nNrlfKlFlUCKT82kuJQMupOaoT1PyaAwfw96GENYAGCDEwuWaAblX375RVcaDgC2jasileTjVztURe8NAJhoyYgsshZGZxnzRH28WCcAqMPhqHi6Epcqv8a61DJuFnQAAFtYDNToYOett96i7777zjytAYBSp/TqdK0TqpsjAwBATYuBGv3Jxotu8jpWPGtxnTp17klQXrhwoSnbBwBmlJ2joeX/3pBtDF8BgCmoImeHVx9/9NFHzdMaAChVey7clmUg/DxcqG31MpZuDgCopBqL2XQ1Fq9bBQDqsCS3CuvhemV1E4EBAKht5XN8ugHYqfSsbFp1TDuEhYU9AcBUPHJXPrfpGZQrV65c6Hw6Fy5cuN82AUAp2HrmFiWmZVGIjxu1qBxk6eYAgEp4KCufZ9hwsDNs2LA8lzMzM+nQoUMyo/KoUaNM2TYAKIUqrJ71w2Q9GwAAU1CqOm062OHSc0OmTZtG+/fvN0WbAMDMeLKv9Se06131boghLAAwHXcrrMYyWc5O9+7d6Z9//jHVwwGAGa07cVM+iCKCPKl+BT9LNwcAVFh6npqhwmDn77//psDAQFM9HACUwlpYPLcO1rQDAHOUnlvTDMpGD2M1atQoz4cjr6sTHR1NsbGxNH36dFO3DwBMLD41g7aejZVtTCQIAOYaxrKmtbGMDnb69OmT57KjoyOVKVOGOnToQJGRkaZsGwCYwapj0ZSZraHIsj5UPdTH0s0BALVOKpiZQzYb7IwbN848LQGA0h3CQmIyAJh1UkHr6dnBpIIAduRmYhrtvnhbtnvVR7ADAKZn02tj8XBVUYmMfHtWlvVEcgCQFy/6qdEQNYkIoPBAT0s3BwBUyMOWVz1ftGhRgbft2rWLvv32W8rJsZ7xOQC419LD1+QcickAYC42XY3Vu3fve647ffo0jR49mpYtW0YDBgyg8ePHm7p9AGAil26l0JGrCcSTJT9cr5ylmwMAKh/GyszWUGZ2Drk4WT5jpkQtuH79Or300ktUr149GbY6fPgwzZ49myIiIkzfQgAw6QrnbaoFUxkfN0s3BwBUPoxlTXk7RgU7CQkJ9O6771K1atXo+PHjtGHDBunVqVu3rvlaCAD3jefDWpw7hNW3UXlLNwcAVMzVyVF6kFlaho0FO1988QVVqVKFli9fTnPnzqWdO3dS27Ztzds6ABXj8ezYpPRSea5/rybQxVsp5O7iSF3rlC2V5wQA++Tg4KBbDNRakpSLnbPDuTkeHh7Sq8NDVnwyZOHChaZsH4BqvTh7P+2+cJumPNlQVh43RlZ2DjkbMQ6+6JC2V6dr7bLk7Wb09FoAAEbPopycnmU1w1jF/tQbOHAg1tABMJHEtEzaef4W5WiI3vrrMDk6OBQraZiDnE9WnqQ5e67QZ/3qUd9GFYp1n+X/avN1+jRCFRYAlF5Fls317MyaNcu8LQGwI4euxEugw7JzNPTG3EPEPyW6FxLw8K+kN+YcpE2ntetafbbqlARIbs7/JQMasv3cLbqVnEGBXq7UtnoZ074QAIBCKrKspfzc8vVgAHZo/6U4Oe/dMIwebVReF/CsPhZtcP/r8XfpsRk7JdBxc3akAE8XupmYTgsPaoenCrM4dwirV/1yVlECCgDq52FlPTv45AOwgH25wU6LykH05eMNqE/DMMrK0dDrcw7S2uN5A55/r8ZT72k76FR0EgV7u9G8V1rR652qy23fbzkvw1QFSUnPojXHb8p2b1RhAYCdLhmBYAeglGVk5dDhqHjZblYpgJwcHeir/g2ll4cDnqFzDtL6E9oAZc3xaOr/wy6p2qoZ6kOLh7amhuH+9FTzcOnduXw7lVYcvVHgc607cVM+bCKCPKlRuH+pvUYAsG+eVrYYKIIdgFJ2/HoCpWXmkL+nC1Ut4y3XScDzeAPq1SBMZh0d8ucBGrPwX3r1jwOyb/saZejvIa2oQoB2PSsu63yhTWXZnr7pPOUoCUAFVGH1blgeBQYAUGrcdcEOenYA7NKBy3fkvGlEADkqM29xtYCTI03u34B61CsnAc/cvVGyaOczLSvSzEFNycfdJc/jDGxVScrIT99Mog2nYu55Hu4N4uRkxsNkAAClxTN3GCsVw1gA9p2v07RS4D23ccDD8+5wcOLq7Ejv96xNE3rXNTinjp+nCz3bSrtEy9RN52SWZH1cbs6Jzw3C/alKbg8SAEBpJihbywzKmF0MoBRxQLL/0h1dvo4hXDE15clG9HlWdpFl5TyU9cv2i3QkKp52nb9NrasF31OFhV4dALBUgjKqsQDsEC/ZcDslQ3pt6pb3K3TfogIdxgt6PtksXLanbT6nu/5CbLKscM65QMbOzgwAYKqeHVRjAdghpVenYQX/YgUzxfFy+6rk7OhAO87dpkNXtI+/OHeF87bVscI5AFiw9Bw9OwD2nK9jeAirJMr7e+hWMp+26bx2hXPdEBbm1gEAC5aeo2cHwP7sz63EamYgOfl+vNqhKnFl+fqTN+mvfVF0JS5VPmy61gk16fMAABR3IVCGnB0AO8Ol4Jyzw0FJ44qm69lhPF/Pw3W162q9v/iYnHetHSrz8QAAlDblswc9OwB25sBl7RAWz4TMZeOmNqRDVTnnWZhZHywPAQAW4uGqDS+QswNgZ/blJiebMl9HH1d3daypXdU82NuVHtArQwcAKE0eLtbVs4M+boBSXunc1Pk6+kZ1i6Rzsck0uE1lgxMRAgCUauk5enaItm7dSr169aKwsDBZt2fx4sV5bueqkg8++IDKlStHHh4e1KVLFzp79myefeLi4mjAgAHk6+tL/v7+NHjwYEpOTi7lVwJQuNSMLDp2PbHAmZNNpXaYL217pxM9l7tuFgCAJaAaS09KSgo1aNCApk2bZvD2L774gr799lv6/vvvac+ePeTl5UXdunWjtLQ03T4c6Bw/fpzWrVtHy5cvlwDq5ZdfLsVXAVC0w1fiZemGMD93KRUHAFAzDyubZ8eiw1jdu3eXkyHcqzNlyhQaO3Ys9e7dW6777bffKDQ0VHqAnnzySTp58iStXr2a9u3bR02bNpV9vvvuO3r44Ydp0qRJ0mMEYF35Oubr1QEAsMYZlHNyNHkWPbYEqx3Uv3jxIkVHR8vQlcLPz49atGhBu3btkst8zkNXSqDDeH9HR0fpCSpIeno6JSYm5jkBmNP+3EqsgtbDAgBQY88OS8/KIUuz2mCHAx3GPTn6+LJyG5+HhITkud3Z2ZkCAwN1+xgyceJECZyUU3i4dm0hAHPIys6hg7mTCaJnBwDsLdhJzcgiS7PaYMecxowZQwkJCbpTVFSUpZsEKnYqOolSMrLJx92ZaoT6WLo5AABmx8NWbs6OVpOkbLXBTtmyZeX85s2bea7ny8ptfB4TE5Pn9qysLKnQUvYxxM3NTaq39E8A5l4Pq0lEgKxCDgBgVxVZGQh2ClS5cmUJWDZs2KC7jnNrOBenVatWcpnP4+Pj6cCBA7p9Nm7cSDk5OZLbA2BNK52bc34dAACrrcjKzLbvaiyeD+fcuXN5kpIPHz4sOTcVK1akYcOG0ccff0zVq1eX4Of999+XCqs+ffrI/rVq1aKHHnqIXnrpJSlPz8zMpNdff10qtVCJBdaAqwp1K51HIDkZAOyvIis1w86Dnf3791PHjh11l0eMGCHngwYNolmzZtE777wjc/HwvDncg/PAAw9Iqbm7u7vuPn/++acEOJ07d5YqrH79+sncPADWICruLsUkpZOLkwM1CPe3dHMAACxSfm7XwU6HDh3kl29BeFbl8ePHy6kg3As0Z84cM7UQ4P4ovTr1yvuRu151AgCA2nlY0cSCVpuzA6Cu+XWQrwMA9sXDNXcxUAQ7AOrFvZZ7Lubm6yDYAQA74+GiDTFSrWAYC8EOgJkCnQnLT9KF2BTJ10FyMgDYG8/cnp009OwAqDPQ+WTFSfplx0W5PKF3XQrwcrV0swAASpWSp2gN1VgIdgBMHOhMXHWKft6uDXQ+7VuPnmxe0dLNAgCw3KSCGMYCUFeg89nqU/Tj1gty+eM+denpFgh0AMDeq7GyLN0UBDsApgp0vlxzmn7Yog10xveuQ8+0jLB0swAALMaa5tlBsANggkDnq7VnaPrm83L5w161aWCrSpZuFgCAVfTspCJnB8D2TV5/lqZu0i578kHP2vRcm8qWbhIAgNXk7KShZwfAti09cp2+3XBWtsf2qEUvPIBABwCAYRgLQAWu3kml/y06KtuvdahKL7atYukmAQBYDQ8MYwHYtqzsHBo+7zAlpWVRw3B/Gv5gDUs3CQDAOnt2MhDsANgkTkbed+kOebs507dPNiIXJ/xXAgDQh3l2AGzYgct36JvcPB0uMa8Y5GnpJgEAWO0MynfRswNgW5LSMmnYvEOUnaOhRxqEUd9G5S3dJAAAq14b6y6CHQDb8sGS4xQVd5cqBHjQx33rkoODg6WbBABg3TMoZyLYAbAZiw9do0WHrpGjA9GUJxqSr7uLpZsEAGD1CcpZORrKyMqxaFsQ7AAUQ1RcKo1dfEy23+hUnZpWCrR0kwAAbKJnxxp6dxDsABSjzPytvw5RcnoWNYkIoDc6VbN0kwAArJ6LkwM5cVe4FeTtINgBKMJP2y7SwSvx5OPmLMNXzigzBwAoEuc0elpJ3g4+tQEKcfFWCk1Zf0a2P+hVm8IDUWYOAFBc7rl5O6kZWWRJCHYACpCTo6HR//xL6Vk51LZ6MD3WpIKlmwQAYFM8rWQxUAQ7AAX4a18U7bkYJ0l2n/athzJzAAAbXR8LwQ6AAdEJaTRx5UnZHtm1BoavAABseH0sBDsA+Wg0Gnp/yTFKSs+iBuH+9HybypZuEgCATfJAgjKAdVp5NJrWnbhJzo4O9Hm/errSSQAAKOFioOjZAbAe8akZNG6pdvLA1zpUpciyvpZuEgCAzS8GmopgB8B6fLziJN1KzqBqId40FJMHAgCYpmcHw1gA1mHb2Vj6+8BV4qIrHr5yc/5vqnMAALiPnB0L9+xo118HsEPpWdl0JyWT4lIy6E5qBr236KhcP7BlBDWJwNpXAAD3y8PV2Sp6dhDsgN1UWC04cJXm7LlCt5LT6U5KBqUY+KUR5udOox6KtEgbAQDUxsNKqrEQ7IDZ3E5Op6mbzlHTiEB6uF5Zi03Kx+0Ys/AorT1x857buNIqwNOFAjxdqayfO73TLZK83fDfAgBATdVY+FQHs5mw/AQtPnydft1xiRpU8KPR3WtRq6pBpdqGjadu0jt/H5XeHF6B963O1al1tWAK9HSlAC9XWdzTEaXlAABmXRsLwQ6o0vHrCRLoKJH9kasJ9NRPu6lTZAi981BNs5d086Jzn6w4SX/uuSKXa4R60+QnGlKdMD+zPi8AAPxHWfU8FdVYoEZfrD4t570ahNGWUR3p2ZYRMknfxlMx1P2bbfT2giN0Pf6uWZ77cFQ89fh2uy7QGfxAZVr6+gMIdAAALLRcRBrm2QG12Xn+Fm05EyvBzdtda1AZHzea0KcurRvRXnJ3NBqSEu+OkzbTzO0XTZqEPGPzeeo3YyddvJVCZX3d6c8XW9D7PWvrJrYCAIDSD3ZSM7PIkjCMBSbFAcfnub06T7eoSBFBXrrbKgd70fQBTejglTv02cpTtPdSnOT1uDo7Ss/P/cjIypEk5H8OXtX1KH3cuy75ebrc5ysCAABbn2cHPTtgUquPRdORqHjJ03mjU3WD+zSuGEDzXmlJb+TOUPzBkmO07Ig2v6ekSzw8O3OPBDpcXcW9SN891QiBDgCAhXlYSbCDnh0wmazsHPpyjbZX58W2VWT4qiBchj7iwRoymd8fu6/QiPmHyc/DhdrVKGPUc/Jw1Quz9sk5l4xPG9CY2hv5GAAAYB5YLgJUZ/7+q3ThVgoFernSS20rF7k/BzwfPVKXetYvR5nZGnrl9wMyxFVcey/GUd/pOyTQKe/vQf8MaY1ABwDAirhjIVBQE+6inLL+jGzz8JSPe/GGkHjY6ev+Dalt9WCJ/LmX5szNpCLvt/DgVRrw826KT82kBuH+tGhoa6pZ1ue+XwcAAJi+Zyc9K4dycjRkKQh2wCR+2XGRYpLSqUKAhyQmG4MTlL9/pgk1DPeX4GXgzL109U7qPftFJ6TR8n+vS9n6iPlHpDeIq7v+eqklhfi4m/DVAACAKauxLD2UhZwduG+8ztT3W87L9ttda5ZotXAvN2f69blm1P+HXXQ2JlkCni8fb0CnohNp/6U7tO9SHF29k3deniEdqtKorjUxAzIAgJVyd84b7PBnvSUg2IH7Nn3zOUpKy6Ja5XzpkQZhJX4cXr7ht8HN6bEZuyT3h+fL0ccxDT9H04gA6lI7lNpWR34OAIA1c3R0IHcXR0rLzLFoRZZqgp1p06bRl19+SdHR0dSgQQP67rvvqHnz5pZulirxGzYuNUN6dG4kpNHsXZflel4G4n57Wcr5edDvg5vT0z/toYS7mdSooj81rRQoAQ5vFzcXCAAArIOnqzOlZWZYdBjLQcOzwNm4efPm0cCBA+n777+nFi1a0JQpU2jBggV0+vRpCgkJKfL+iYmJ5OfnRwkJCeTra941m+5XQmomXYlLpUBvVyrn626WIZzEtEy6EJtC52OS6Xys9hQVd1fKxPnEEXp+LasE0tyXWppsZXMuY2fOTkgrAwCwZbFJ6eTm4kjerqZfeLm439+qCHY4wGnWrBlNnTpVLufk5FB4eDi98cYbNHr0aIsFOx8uPS5JtYVVIvHEd8oK3IFeLhTgyeeuEglH3UnNDThSJOC4EJtMt5Iz8kzWxLMSVw3xpqplvKhqGW+qUsZL5qsxhP/SHFlzjwwHLXEpmdoAJiVDemp4rSoOcjjRuCiuTo4UkNveUF93er9nLaoWgmooAAAoPcX9/rb5YayMjAw6cOAAjRkzRnedo6MjdenShXbt2mXwPunp6XLSP1jmsPVsrAQPphbs7SpVSxy4nLiRKCdTC/Fx0wVPfF4p2JOCvNwkEOPAzMvVyWS9OAAAAOZk88HOrVu3KDs7m0JDQ/Ncz5dPnTpl8D4TJ06kjz76yOxte6tzdUpMyyp0qIaDFm0vS4Zs8zlfTk7LojB/D6oa8l+PjfbcW2YKzszOoai41Dy9PrzN54VN3sQTPAXlBizaXiRt7wxfVgKcymW8yBe5MQAAoBI2H+yUBPcCjRgxIk/PDg97mVrvhuXJXFycHCXw4dODlDfQAwAAABUFO8HBweTk5EQ3b97Mcz1fLlu2rMH7uLm5yQkAAADUz+ZLXVxdXalJkya0YcMG3XWcoMyXW7VqZdG2AQAAgOXZfM8O4yGpQYMGUdOmTWVuHS49T0lJoeeff97STQMAAAALU0Ww88QTT1BsbCx98MEHMqlgw4YNafXq1fckLQMAAID9UcU8O/fLliYVBAAAAOO+v20+ZwcAAACgMAh2AAAAQNUQ7AAAAICqIdgBAAAAVUOwAwAAAKqGYAcAAABUDcEOAAAAqBqCHQAAAFA1BDsAAACgaqpYLuJ+KZNI80yMAAAAYBuU7+2iFoNAsENESUlJch4eHm7ppgAAAEAJvsd52YiCYG0sIsrJyaHr16+Tj48POTg4mDTi5AAqKioKa24ZgONTMBybwuH4FAzHpnA4Puo6PhzCcKATFhZGjo4FZ+agZ4cTlxwdqUKFCmZ7fH7D2MKbxlJwfAqGY1M4HJ+C4dgUDsdHPcensB4dBRKUAQAAQNUQ7AAAAICqIdgxIzc3Nxo3bpycw71wfAqGY1M4HJ+C4dgUDsfHPo8PEpQBAABA1dCzAwAAAKqGYAcAAABUDcEOAAAAqBqCHQAAAFA1BDtF2Lp1K/Xq1UtmZ+TZlRcvXpzn9ps3b9Jzzz0nt3t6etJDDz1EZ8+eNfhYnAvevXt3g4+zb98+6ty5M/n7+1NAQAB169aNjhw5Qmo/PpcuXZL7GTotWLBA9rl9+7bcjx+DKwR4ds/XX3/d6tcyM8V7Jzo6mp599lkqW7YseXl5UePGjemff/7Js88jjzxCFStWJHd3dypXrpzszzOCWztTHJ/z589T3759qUyZMjIBWv/+/eV+tn58Jk6cSM2aNZNZ3UNCQqhPnz50+vTpPPukpaXR0KFDKSgoiLy9valfv373vPYrV65Qjx495Pjx44waNYqysrJ0t2/fvp3atGkjj+Hh4UGRkZE0efJksnamOj5vvvkmNWnSRD5XGjZseM/z8GN27NiRQkND5f1TpUoVGjt2LGVmZpKaj82RI0foqaeeks9afl/UqlWLvvnmmzyPYWvvHQQ7RUhJSaEGDRrQtGnTDAYv/Ea6cOECLVmyhA4dOkQRERHUpUsXuV9+U6ZMMbgcRXJysnyQ8wfynj175E3Eb1QOeKz5P5Upjg//Z7px40ae00cffST/ATkwVGa47t27Ny1dupTOnDlDs2bNovXr19Orr75Kan/vDBw4UD6o+LUfPXqUHn30UflC5/0V/GE8f/582Y8DIQ4AHnvsMbJ293t8+Lxr167yf2rjxo20Y8cOysjIkACKl4Cx5eOzZcsW+TLavXs3rVu3Tj4H+LXqvzeGDx9Oy5Ytkx8FvD8HcPz+UGRnZ0ugw8dk586dNHv2bPm/88EHH+j24QCafzhw4Hny5En5IufTjz/+SGo/PooXXniBnnjiCYPP4+LiIv8H165dK+8f/gz/6aefpDRbzcfmwIEDEij98ccfdPz4cfrf//5HY8aMoalTp9rue4dLz6F4+HAtWrRId/n06dNy3bFjx3TXZWdna8qUKaP56aef8tz30KFDmvLly2tu3Lhxz+Ps27dPrrty5Yruun///VeuO3v2rMYejo++hg0bal544YVCn+ubb77RVKhQQaP2Y+Pl5aX57bff8jxWYGBgocdvyZIlGgcHB01GRoZGzcdnzZo1GkdHR01CQoJun/j4eHnt69atU9XxiYmJkeOxZcsW3et0cXHRLFiwQLfPyZMnZZ9du3bJ5ZUrV8rxiY6O1u0zY8YMja+vryY9Pb3A5+rbt6/mmWee0diSkhwffePGjdM0aNCgWM81fPhwzQMPPKCxl2OjeO211zQdO3bUFMaa3zvo2bkP6enpcs7dmwruheAuUe6dUaSmptLTTz8tv2B5OCK/mjVrSlfgzJkz5VfY3bt3ZZu7DitVqkRqPz76+BfF4cOHafDgwQU+Lv8KWbhwIbVv357Ufmxat25N8+bNo7i4OOmt+Ouvv6QLukOHDgYfl/f7888/5X78q1TNx4f34V4d/cnPeH/er6D3l60en4SEBDkPDAzU/T/hX+zc06XgYQTuHd61a5dc5vN69erJEIyCe4t5+Jd/rRvCPWjcC2Rr/7dKcnxK4ty5c7R69WqbOj6mOjYJCQm6x7DF9w6CnfugvEG4e+/OnTsSqHz++ed09epVGY7R7zLkD1ceijGEh6w2b94sXYY89slDOPwfatWqVeTs7Kz646NPCfL4eOXHY8ice1C+fHnJz/j5559J7ceGh1/4g4mDYf5Sf+WVV2jRokVUrVq1PI/37rvvSrcy78d5Gjz0Y8uKc3xatmwpr5lfO/+g4G76t99+W4Zv8r+/bPn4cJA7bNgwyY+oW7euLpfL1dVVcvz0cWDDtyn76Ac6yu3Kbfp4IWR+fzVt2lSGQF588UVS+/ExBn8ecSBdvXp1atu2LY0fP57s6djs3LlTfnS9/PLL99xmK+8dBDv3gX8Zcg8D55FwxMtfxJs2bZJcE2Wpec614HwCHustCPfkcE8GvyF5nJVzD/iNyePtfJuaj48+fq1z5swpsFeHk98OHjwoX1ScdzFixAhS+7F5//33KT4+XnKU9u/fL6+Zc3Y4f0cfJ57yLyvOLXBycpI8A1ueHL04x4eTkjnngHMP+AcCr3zMx4qTuPO/v2z5+PAXyLFjx6RXz1y2bdsm76/vv/9ePqvmzp1LtqI0jg9/0fNnD38+rVixgiZNmkT2cmyOHTsmP9Q5T4lzf2z2vWPpcTRbkj+vQB+Pg/LYKGvevLmMb7K33npL8gOcnJx0J34cHktv37697PPzzz9rQkJCJCdBwWPqnp6emrlz52rUfHz0cW4KjyUr+xVm27Zt8nzXr1/XqPXYnDt37p68Fda5c2fNK6+8UuBzRUVFyf127typsZf3TmxsrObOnTuyHRoaqvniiy9UcXyGDh0quWkXLlzIc/2GDRvkNSivWVGxYkXN119/Ldvvv//+PXko/Dh8v4MHDxb4nBMmTNDUqFFDYwvu5/iUNGfn999/13h4eGiysrI0aj82x48fl++m9957r1jPac3vHfTsmAj/quRfmlway1GuMmQ1evRo+vfffyUPRTkpvRS//vqrbHMXPP8S1a/UUi7rV5Wo8fjkH8LiMmHeryjKcVFyO9R4bPh9wfL3UnDPRGHvCzUdm+K+d4KDg6VbnntRY2Ji5H1ky8eH4z+udOEhS35NlStXznM7l0tz79eGDRt013G1EA/RtWrVSi7zOfcA8vFQcHUODwHXrl270ONjzcfGVMenpPj48NCytX42m+rYHD9+XCoZBw0aRJ988kmxntuq3zuWjrasXVJSklRS8YkPF0e+vH358mW5ff78+ZpNmzZpzp8/r1m8eLEmIiJC8+ijjxr1K5Yz4d3c3DRDhgzRnDhxQn7Jc0a7n5+f1fdcmOr4cNUZ94CtWrXqnttWrFih+eWXXzRHjx7VXLx4UbN8+XJNrVq1NG3atNGo+dhwtVC1atU0bdu21ezZs0d6eiZNmiTHiY8J2717t+a7776Tx7106ZL8amvdurWmatWqmrS0NI3a3zv8vuAKEj42/IubK9VGjBihu91Wjw9/FvD//82bN0sFp3JKTU3V7fPqq6/Kr/GNGzdq9u/fr2nVqpWcFNzzULduXU3Xrl01hw8f1qxevVqq2caMGaPbZ+rUqZqlS5dqzpw5IyfuZfbx8dH873//01gzUxwf5XOH3xvcU8o9Esr7UalW++OPPzTz5s2Tz2V+H/J2WFiYZsCAARo1H5ujR4/Ke4W/h/QfQ7/X3dbeOwh2isAftvxBnP80aNCgPCXQPPzCb56xY8cWWtZZUJf92rVr5cub36QBAQGaTp06FVoGqLbjwx/A4eHheYbyFPwfkv8j8rFxd3fXVK9eXfPuu+/e0w2rxmPDHyL8Bc9dyTysWb9+/Tyl6DxFAZeD8pc8B8yVKlWSD7KrV69qrJ0pjg+/D3jYivfh98VXX32lycnJsfnjY+i48OnXX3/V7XP37l0Z0uPPC35vcNkvfyHp4wCve/fuMuwSHBysGTlypCYzM1N3+7fffqupU6eO3J9L0hs1aqSZPn26wf+Hajw+nEpg6HH4RxX766+/NI0bN9Z4e3vLNBC1a9fWfPrpp/LYaj4248aNM/gY/IPDVt87DvyPpXuXAAAAAMwFOTsAAACgagh2AAAAQNUQ7AAAAICqIdgBAAAAVUOwAwAAAKqGYAcAAABUDcEOAAAAqBqCHQBQHZ4+rEuXLrJKNS/XwtsXL160dLMAwEIQ7ACATdq1a5esE9ajR497brt06ZLcNnXqVHr22Wdl3az8awQBgP3ADMoAYJNefPFF8vb2lgVkeSHDsLAwSzcJAKwUenYAwOYkJyfTvHnzaMiQIdKzM2vWLN1tmzdvJgcHB1nVuWnTpuTp6UmtW7eWgEjfjBkzqGrVquTq6ko1a9ak33//3QKvBABKA4IdALA58+fPp8jISAlSnnnmGfrll18kT0ff//73P/rqq69o//795OzsTC+88ILutkWLFtFbb71FI0eOpGPHjtErr7xCzz//PG3atMkCrwYAzA3DWABgc9q0aUP9+/eXgCUrK4vKlStHCxYsoA4dOkjPTseOHWn9+vXUuXNn2X/lypXSA3T37l1yd3eX+9epU4d+/PFH3WPy46WkpNCKFSss+MoAwBzQswMANoWHo/bu3UtPPfWUXOZemyeeeEJyd/TVr19ft83BEIuJiZHzkydPSsCjjy/z9QCgPs6WbgAAgDE4qOHeHP2EZO6gdnNzk+orhYuLi26bc3hYTk5OKbcWAKwBenYAwGZwkPPbb79JLs7hw4d1pyNHjkjwM3fu3GI9Tq1atWjHjh15ruPLtWvXNlPLAcCS0LMDADZj+fLldOfOHRo8eDD5+fnlua1fv37S6/Pll18W+TijRo2SHJ1GjRrJhIPLli2jhQsXSp4PAKgPenYAwGZwMMPBSf5ARwl2uPKKZ0wuSp8+feibb76hSZMmSaLyDz/8QL/++qskOAOA+qAaCwAAAFQNPTsAAACgagh2AAAAQNUQ7AAAAICqIdgBAAAAVUOwAwAAAKqGYAcAAABUDcEOAAAAqBqCHQAAAFA1BDsAAACgagh2AAAAQNUQ7AAAAICqIdgBAAAAUrP/AxMRFi0WApgWAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "juegos_por_año.plot()\n",
    "plt.xlabel(\"Año\")\n",
    "plt.ylabel(\"Numero de juegos por año\")\n",
    "plt.title(\"Cantidad de juegos por año\")\n",
    "plt.show()    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "La producción de videojuegos muestra un crecimiento significativo a partir de los años 80, coincidiendo con la popularización de consolas domésticas. El crecimiento se acelera en los 90 con avances tecnológicos y alcanza su mayor expansión después de 2005, impulsado por la distribución digital y el desarrollo independiente"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ¿Mas producción igual a menos calidad?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>averageRating</th>\n",
       "      <th>cantidadJuegos</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>startYear</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1979</th>\n",
       "      <td>4.555769</td>\n",
       "      <td>52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1980</th>\n",
       "      <td>4.822857</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1981</th>\n",
       "      <td>5.308434</td>\n",
       "      <td>83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1982</th>\n",
       "      <td>5.355072</td>\n",
       "      <td>138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1983</th>\n",
       "      <td>5.964000</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           averageRating  cantidadJuegos\n",
       "startYear                               \n",
       "1979            4.555769              52\n",
       "1980            4.822857              70\n",
       "1981            5.308434              83\n",
       "1982            5.355072             138\n",
       "1983            5.964000             125"
      ]
     },
     "execution_count": 156,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "comparativa = ratings_anuales.to_frame().join(juegos_por_año.to_frame(name = \"cantidadJuegos\"))\n",
    "\n",
    "comparativa = comparativa[comparativa[\"cantidadJuegos\"] > 50]\n",
    "\n",
    "comparativa.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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9ufMmTNmyQj3GwAAcK6gg5tnnnlGXnrpJZk9e7ZJJNb8G82Ruf3226VChQpBPVeLFi1MHs28efNkwoQJsnv3bmnTpo2cOHHC5/Gaj/P222/L559/LlOnTpWLFy+aQOuXX37J8DXGjh1rgi77pkERAABwrgRLhz8FoVChQqa1pFKlSlKyZEn55ptvpF69eqYlp127dmYNqqw6duyYaZV58cUXpW/fvpker61GtWvXlu7du8uYMWMybLnRm01bbjTASUtLY5FPAABihF6/tZEikOt30Dk3uoim3bJSrlw52bhxowluNDA5depU1kstYhblrFGjhuzYsSOg4/PmzSuNGjXye7yOptIbAACID0F3S1199dUyf/588//bbrtNBg8eLPfee69pPWnfvn22CqP5NDt37pTk5OSAjtfJA3XOnUCPBwAAzhd0y82rr77qmlfmscceM60ny5cvl1tvvVUef/zxoJ5LJ/3r2rWr6Yo6ePCgjBgxQnLnzm0CJdWrVy/TOqR5M2r06NHSsmVLqVatmmkpGjdunOzdu1fuueeeYN8GAABwqKCDmxIlSrj+nytXLhk6dKjr/unTp4N6Lk0E1kDm999/l1KlSslVV10l33//vfm/0pFT+hq2o0ePmlaiQ4cOme6xJk2amMAqJSUl2LcBAAAcKuiEYl80Yfe1116T559/3gQeTklIAgAAsXf9zhVMADNs2DBp2rSpGX49c+ZM14zFlStXNsPDH3rooeyXHgAAICe6pZ588kl54403pEOHDqYrSJOJdZ0n7UbSodt6X/NlAAAAYiK4mT59urz77rty4403muHf9evXl/Pnz8uPP/7I+k4AACBq5Aom+VcTeFXdunXN3DHaDUVgAwAAYjK40TlldLkF9wUvL7vssnCVCwAAILzdUjqoqk+fPq7ZfnWum379+pnlGLKzKjgAAEBEgpvevXt73O/Zs2dICwIAAJCjwY0O+QaCdeGiJat2H5HDJ9KldOFEaV65hOTORZ4WACCKZigGAjVvY6qMmr1ZUtP+u1yHSi6aKCO6pkjnuqwHBgCIkoUzgUADm/5T13oENupQWrrZrvsBAAgHghuEpStKW2x8rethb9P9ehwAAKFGcIOQ0xwb7xYbdxrS6H49DgCAUCO4Qchp8nAojwMAIBgkFMeQWBl5pGUL5XEAAASD4CZGxNLIIw26tGyaPOwr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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure()\n",
    "plt.scatter(comparativa[\"cantidadJuegos\"], comparativa[\"averageRating\"])\n",
    "plt.xlabel(\"Cantidad de juegos por año\")\n",
    "plt.ylabel(\"Rating promedio\")\n",
    "plt.title(\"Producción vs Calidad promedio\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>averageRating</th>\n",
       "      <th>cantidadJuegos</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>averageRating</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.807845</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>cantidadJuegos</th>\n",
       "      <td>0.807845</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                averageRating  cantidadJuegos\n",
       "averageRating        1.000000        0.807845\n",
       "cantidadJuegos       0.807845        1.000000"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "comparativa.corr()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Se observó una correlación positiva (0.77) entre el volumen anual de lanzamientos y el rating promedio. Esto sugiere que el crecimiento de la industria ha estado acompañado por mejoras en los estándares de calidad, posiblemente impulsadas por avances tecnológicos, profesionalización del desarrollo y mayor competencia."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
