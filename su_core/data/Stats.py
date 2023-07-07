from enum import Enum, auto


class Stat(Enum):
    Invalid = -1
    Strength = 0
    Energy = auto()
    Dexterity = auto()
    Vitality = auto()
    StatPoints = auto()
    SkillPoints = auto()
    Life = auto()
    MaxLife = auto()
    Mana = auto()
    MaxMana = auto()
    Stamina = auto()
    MaxStamina = auto()
    Level = auto()
    Experience = auto()
    Gold = auto()
    StashGold = auto()
    EnhancedDefense = auto()
    EnhancedDamageMax = auto()
    EnhancedDamage = auto()
    AttackRating = auto()
    ChanceToBlock = auto()
    MinDamage = auto()
    MaxDamage = auto()
    TwoHandedMinDamage = auto()
    TwoHandedMaxDamage = auto()
    DamagePercent = auto()
    ManaRecovery = auto()
    ManaRecoveryBonus = auto()
    StaminaRecoveryBonus = auto()
    LastExp = auto()
    NextExp = auto()
    Defense = auto()
    DefenseVsMissiles = auto()
    DefenseVsHth = auto()
    NormalDamageReduction = auto()
    MagicDamageReduction = auto()
    DamageReduced = auto()
    MagicResist = auto()
    MaxMagicResist = auto()
    FireResist = auto()
    MaxFireResist = auto()
    LightningResist = auto()
    MaxLightningResist = auto()
    ColdResist = auto()
    MaxColdResist = auto()
    PoisonResist = auto()
    MaxPoisonResist = auto()
    DamageAura = auto()
    FireMinDamage = auto()
    FireMaxDamage = auto()
    LightningMinDamage = auto()
    LightningMaxDamage = auto()
    MagicMinDamage = auto()
    MagicMaxDamage = auto()
    ColdMinDamage = auto()
    ColdMaxDamage = auto()
    ColdLength = auto()
    PoisonMinDamage = auto()
    PoisonMaxDamage = auto()
    PoisonLength = auto()
    LifeSteal = auto()
    LifeStealMax = auto()
    ManaSteal = auto()
    ManaStealMax = auto()
    StaminaDrainMinDamage = auto()
    StaminaDrainMaxDamage = auto()
    StunLength = auto()
    VelocityPercent = auto()
    AttackRate = auto()
    OtherAnimRate = auto()
    Quantity = auto()
    Value = auto()
    Durability = auto()
    MaxDurability = auto()
    ReplenishLife = auto()
    MaxDurabilityPercent = auto()
    MaxLifePercent = auto()
    MaxManaPercent = auto()
    AttackerTakesDamage = auto()
    GoldFind = auto()
    MagicFind = auto()
    Knockback = auto()
    TimeDuration = auto()
    AddClassSkills = auto()
    Unused84 = auto()
    AddExperience = auto()
    LifeAfterEachKill = auto()
    ReducePrices = auto()
    DoubleHerbDuration = auto()
    LightRadius = auto()
    LightColor = auto()
    Requirements = auto()
    LevelRequire = auto()
    IncreasedAttackSpeed = auto()
    LevelRequirePercent = auto()
    LastBlockFrame = auto()
    FasterRunWalk = auto()
    NonClassSkill = auto()
    State = auto()
    FasterHitRecovery = auto()
    PlayerCount = auto()
    PoisonOverrideLength = auto()
    FasterBlockRate = auto()
    BypassUndead = auto()
    BypassDemons = auto()
    FasterCastRate = auto()
    BypassBeasts = auto()
    SingleSkill = auto()
    SlainMonstersRestInPeace = auto()
    CurseResistance = auto()
    PoisonLengthReduced = auto()
    NormalDamage = auto()
    HitCausesMonsterToFlee = auto()
    HitBlindsTarget = auto()
    DamageTakenGoesToMana = auto()
    IgnoreTargetsDefense = auto()
    TargetDefense = auto()
    PreventMonsterHeal = auto()
    HalfFreezeDuration = auto()
    AttackRatingPercent = auto()
    MonsterDefensePerHit = auto()
    DemonDamagePercent = auto()
    UndeadDamagePercent = auto()
    DemonAttackRating = auto()
    UndeadAttackRating = auto()
    Throwable = auto()
    FireSkills = auto()
    AllSkills = auto()
    AttackerTakesLightDamage = auto()
    IronMaidenLevel = auto()
    LifeTapLevel = auto()
    ThornsPercent = auto()
    BoneArmor = auto()
    BoneArmorMax = auto()
    FreezesTarget = auto()
    OpenWounds = auto()
    CrushingBlow = auto()
    KickDamage = auto()
    ManaAfterKill = auto()
    HealAfterDemonKill = auto()
    ExtraBlood = auto()
    DeadlyStrike = auto()
    AbsorbFirePercent = auto()
    AbsorbFire = auto()
    AbsorbLightningPercent = auto()
    AbsorbLightning = auto()
    AbsorbMagicPercent = auto()
    AbsorbMagic = auto()
    AbsorbColdPercent = auto()
    AbsorbCold = auto()
    SlowsTarget = auto()
    Aura = auto()
    Indestructible = auto()
    CannotBeFrozen = auto()
    SlowerStaminaDrain = auto()
    Reanimate = auto()
    Pierce = auto()
    MagicArrow = auto()
    ExplosiveArrow = auto()
    ThrowMinDamage = auto()
    ThrowMaxDamage = auto()
    SkillHandofAthena = auto()
    SkillStaminaPercent = auto()
    SkillPassiveStaminaPercent = auto()
    SkillConcentration = auto()
    SkillEnchant = auto()
    SkillPierce = auto()
    SkillConviction = auto()
    SkillChillingArmor = auto()
    SkillFrenzy = auto()
    SkillDecrepify = auto()
    SkillArmorPercent = auto()
    Alignment = auto()
    Target0 = auto()
    Target1 = auto()
    GoldLost = auto()
    ConverisonLevel = auto()
    ConverisonMaxHP = auto()
    UnitDooverlay = auto()
    AttackVsMonType = auto()
    DamageVsMonType = auto()
    Fade = auto()
    ArmorOverridePercent = auto()
    Unused183 = auto()
    Unused184 = auto()
    Unused185 = auto()
    Unused186 = auto()
    Unused187 = auto()
    AddSkillTab = auto()
    Unused189 = auto()
    Unused190 = auto()
    Unused191 = auto()
    Unused192 = auto()
    Unused193 = auto()
    NumSockets = auto()
    SkillOnAttack = auto()
    SkillOnKill = auto()
    SkillOnDeath = auto()
    SkillOnHit = auto()
    SkillOnLevelUp = auto()
    Unused200 = auto()
    SkillOnGetHit = auto()
    Unused202 = auto()
    Unused203 = auto()
    ItemChargedSkill = auto()
    Unused205 = auto()
    Unused206 = auto()
    Unused207 = auto()
    Unused208 = auto()
    Unused209 = auto()
    Unused210 = auto()
    Unused211 = auto()
    Unused212 = auto()
    Unused213 = auto()
    DefensePerLevel = auto()
    ArmorPercentPerLevel = auto()
    LifePerLevel = auto()
    ManaPerLevel = auto()
    MaxDamagePerLevel = auto()
    MaxDamagePercentPerLevel = auto()
    StrengthPerLevel = auto()
    DexterityPerLevel = auto()
    EnergyPerLevel = auto()
    VitalityPerLevel = auto()
    AttackRatingPerLevel = auto()
    AttackRatingPercentPerLevel = auto()
    ColdDamageMaxPerLevel = auto()
    FireDamageMaxPerLevel = auto()
    LightningDamageMaxPerLevel = auto()
    PoisonDamageMaxPerLevel = auto()
    ResistColdPerLevel = auto()
    ResistFirePerLevel = auto()
    ResistLightningPerLevel = auto()
    ResistPoisonPerLevel = auto()
    AbsorbColdPerLevel = auto()
    AbsorbFirePerLevel = auto()
    AbsorbLightningPerLevel = auto()
    AbsorbPoisonPerLevel = auto()
    ThornsPerLevel = auto()
    ExtraGoldPerLevel = auto()
    MagicFindPerLevel = auto()
    RegenStaminaPerLevel = auto()
    StaminaPerLevel = auto()
    DamageDemonPerLevel = auto()
    DamageUndeadPerLevel = auto()
    AttackRatingDemonPerLevel = auto()
    AttackRatingUndeadPerLevel = auto()
    CrushingBlowPerLevel = auto()
    OpenWoundsPerLevel = auto()
    KickDamagePerLevel = auto()
    DeadlyStrikePerLevel = auto()
    FindGemsPerLevel = auto()
    ReplenishDurability = auto()
    ReplenishQuantity = auto()
    ExtraStack = auto()
    FindItem = auto()
    SlashDamage = auto()
    SlashDamagePercent = auto()
    CrushDamage = auto()
    CrushDamagePercent = auto()
    ThrustDamage = auto()
    ThrustDamagePercent = auto()
    AbsorbSlash = auto()
    AbsorbCrush = auto()
    AbsorbThrust = auto()
    AbsorbSlashPercent = auto()
    AbsorbCrushPercent = auto()
    AbsorbThrustPercent = auto()
    ArmorByTime = auto()
    ArmorPercentByTime = auto()
    LifeByTime = auto()
    ManaByTime = auto()
    MaxDamageByTime = auto()
    MaxDamagePercentByTime = auto()
    StrengthByTime = auto()
    DexterityByTime = auto()
    EnergyByTime = auto()
    VitalityByTime = auto()
    AttackRatingByTime = auto()
    AttackRatingPercentByTime = auto()
    ColdDamageMaxByTime = auto()
    FireDamageMaxByTime = auto()
    LightningDamageMaxByTime = auto()
    PoisonDamageMaxByTime = auto()
    ResistColdByTime = auto()
    ResistFireByTime = auto()
    ResistLightningByTime = auto()
    ResistPoisonByTime = auto()
    AbsorbColdByTime = auto()
    AbsorbFireByTime = auto()
    AbsorbLightningByTime = auto()
    AbsorbPoisonByTime = auto()
    FindGoldByTime = auto()
    MagicFindByTime = auto()
    RegenStaminaByTime = auto()
    StaminaByTime = auto()
    DamageDemonByTime = auto()
    DamageUndeadByTime = auto()
    AttackRatingDemonByTime = auto()
    AttackRatingUndeadByTime = auto()
    CrushingBlowByTime = auto()
    OpenWoundsByTime = auto()
    KickDamageByTime = auto()
    DeadlyStrikeByTime = auto()
    FindGemsByTime = auto()
    PierceCold = auto()
    PierceFire = auto()
    PierceLightning = auto()
    PiercePoison = auto()
    DamageVsMonster = auto()
    DamagePercentVsMonster = auto()
    AttackRatingVsMonster = auto()
    AttackRatingPercentVsMonster = auto()
    AcVsMonster = auto()
    AcPercentVsMonster = auto()
    FireLength = auto()
    BurningMin = auto()
    BurningMax = auto()
    ProgressiveDamage = auto()
    ProgressiveSteal = auto()
    ProgressiveOther = auto()
    ProgressiveFire = auto()
    ProgressiveCold = auto()
    ProgressiveLightning = auto()
    ExtraCharges = auto()
    ProgressiveAttackRating = auto()
    PoisonCount = auto()
    DamageFrameRate = auto()
    PierceIdx = auto()
    FireSkillDamage = auto()
    LightningSkillDamage = auto()
    ColdSkillDamage = auto()
    PoisonSkillDamage = auto()
    EnemyFireResist = auto()
    EnemyLightningResist = auto()
    EnemyColdResist = auto()
    EnemyPoisonResist = auto()
    PassiveCriticalStrike = auto()
    PassiveDodge = auto()
    PassiveAvoid = auto()
    PassiveEvade = auto()
    PassiveWarmth = auto()
    PassiveMasteryMeleeAttackRating = auto()
    PassiveMasteryMeleeDamage = auto()
    PassiveMasteryMeleeCritical = auto()
    PassiveMasteryThrowAttackRating = auto()
    PassiveMasteryThrowDamage = auto()
    PassiveMasteryThrowCritical = auto()
    PassiveWeaponBlock = auto()
    SummonResist = auto()
    ModifierListSkill = auto()
    ModifierListLevel = auto()
    LastSentHPPercent = auto()
    SourceUnitType = auto()
    SourceUnitID = auto()
    ShortParam1 = auto()
    QuestItemDifficulty = auto()
    PassiveMagicMastery = auto()
    PassiveMagicPierce = auto()
