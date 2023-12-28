# Insolvenzen und Geschaeftsaufgaben in Deutschland

In late 2022 some germans had more worries about an "Insolvency wave" during the winter.
There was an interview with german minster of economy `Robert Habeck` saying companies will stop producing, but now go insolvent.

Now, there was very little context, that's why we will look at the insolvency rates AND at the rates for people giving up their businesses.


## 🏗️ Usage

```BASH
python3 -m venv Env
source Env/bin/activate

python3 insolvency_in_germany/visualize_germany_insolvency_data.py
```

---

Last run December 2023.
Data until September 2023
![](data/Insolvencies_in_Germany.png)

## 🚧 Problems
- Add legend to graphs!
-


1. Insolvenzen URL:https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/Gewerbemeldungen-Insolvenzen/Tabellen/Insolvenzen.html#241898
Insolvenzen seit 1953: https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/Gewerbemeldungen-Insolvenzen/Tabellen/lrins01.html#242428

2. Per API?

- Get all insolvencies by month (or year?) beyond 2007 to include the financial crisis


## Vorgehen
1. Get table from URL/Page
2. PD Dataframe extract



## ❓️Open Questions


### What are these categories?
Alle exklusiv.

- Unternehmen:
- Verbraucher: **Privatinsolvenz**
- ehemals selbständig Tätige
- sonstige natürliche Personen, Nachlässe

### Regelinsolvenzverfahren?
- Für Selbständige und Freiberufler
- vereinfachtes Insolvenzverfahren für zahlungsunfähige natürliche Person

🔗 URL: https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/Gewerbemeldungen-Insolvenzen/_inhalt.html