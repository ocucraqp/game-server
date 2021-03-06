# DB

## accounts.User(ユーザー)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|ユーザー名|username|CharField|50字以下, unique=True|
|パスワード|password|CharField|128字以下|
|所持金|money|IntegerField|default=0|
|ステータスポイント|st_point|IntegerField|default=0|
|最大体力|status_hp|IntegerField|default=10|
|腕力|status_arm|IntegerField|default=1|
|筋力|status_muscle|IntegerField|default=1, 後で実装|
|幸運|status_luck|IntegerField|default=1|
|体力|hp|IntegerField|default=1|
|武器|weapon|ForeignKey|Weapon|
|頭防具|equipment_head|ForeignKey|Equipment, 後で実装|
|胴体防具|equipment_body|ForeignKey|Equipment, 後で実装|
|腕防具|equipment_arm|ForeignKey|Equipment, 後で実装|
|足防具|equipment_leg|ForeignKey|Equipment, 後で実装|

## equipments.Weapon(武器)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|名前|name|CharField|100字以下|
|攻撃力|atk|IntegerField|default=1|
|値段|price|IntegerField|default=0|
|必要腕力|required_arm|IntegerField|default=1|

## equipments.Equipment(防具) (後で実装)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|名前|name|CharField|100字以下|
|防御力|def|IntegerField|default=1|
|値段|price|IntegerField|default=0|
|種類|type|CharField|choiceで設定|
|必要筋力|required_muscle|IntegerField|default=1|

type=['head','body','arm','leg']

## battles.EnemyType(敵の種類)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|名前|name|CharField|100字以下|
|最大体力|status_hp|IntegerField|default=1|
|攻撃力|atk|IntegerField|default=1|
|報酬金|reward_money|IntegerField|default=1|
|報酬ステータスポイント|reward_st_point|IntegerField|default=1|
|画像|image|ImageField||
|有効|enabled|BooleanField|default=True, falseのときはこの敵を生成しない|

## battles.Enemy(敵)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|種類|type|ForeignKey|EnemyType|
|体力|hp|IntegerField|default=EnemyType.status_hp|

## battles.Contribution(貢献度)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|敵|enemy|ForeignKey|Enemy|
|ユーザー|user|ForeignKey|User|
|貢献ダメージ|damage|IntegerField|default=0|
|受け取り済み|received|BooleanField|default=false, 報酬確認されたときTrueに|
