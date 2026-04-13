from sqlalchemy.orm import Session
from app.database.db import engine, SQLAlchemyBase
from app.models.user import User
from app.models.ancestor_data import Clan, AncestorData, Application, Match, AncestorDataStatus, ApplicationStatus
from app.models.genealogy import Genealogy, GenealogyMember, GenealogyDocument, GenealogyUserPermission, GenealogyStatus, GenealogyPermission
from app.models.interaction import ChatRoom, Message, Activity, ActivityParticipant, CultureShare, ZongQinCard
import uuid
from datetime import datetime, timedelta
import bcrypt


def get_password_hash(password):
    # 确保密码长度不超过72字节
    if len(password) > 72:
        password = password[:72]
    # 使用bcrypt直接哈希密码
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')


def init_database():
    """初始化数据库"""
    # 创建所有表
    SQLAlchemyBase.metadata.create_all(bind=engine)
    
    # 创建数据库会话
    db = Session(bind=engine)
    
    try:
        # 检查是否已经有数据
        if db.query(User).count() > 0:
            print("数据库已经初始化，跳过...")
            return
        
        print("开始初始化数据库...")
        
        # 1. 创建测试用户
        users = [
            User(
                id=str(uuid.uuid4()),
                username="admin",
                email="admin@example.com",
                hashed_password=get_password_hash("123456"),
                real_name="管理员",
                is_admin=True,
                is_verified=True
            ),
            User(
                id=str(uuid.uuid4()),
                username="user1",
                email="user1@example.com",
                hashed_password=get_password_hash("123456"),
                real_name="张三",
                surname="张",
                is_verified=True
            ),
            User(
                id=str(uuid.uuid4()),
                username="user2",
                email="user2@example.com",
                hashed_password=get_password_hash("123456"),
                real_name="李四",
                surname="李",
                is_verified=True
            ),
            User(
                id=str(uuid.uuid4()),
                username="user3",
                email="user3@example.com",
                hashed_password=get_password_hash("123456"),
                real_name="王五",
                surname="王",
                is_verified=True
            )
        ]
        db.add_all(users)
        db.commit()
        print(f"创建了 {len(users)} 个用户")
        
        # 2. 创建宗族
        clans = [
            Clan(
                id=str(uuid.uuid4()),
                name="张氏宗族",
                surname="张",
                hall_name="清河堂",
                origin="河北省清河县",
                description="张氏宗族是中国最大的姓氏之一，起源于河北省清河县。"
            ),
            Clan(
                id=str(uuid.uuid4()),
                name="李氏宗族",
                surname="李",
                hall_name="陇西堂",
                origin="甘肃省陇西县",
                description="李氏宗族起源于甘肃省陇西县，是中国人口最多的姓氏。"
            ),
            Clan(
                id=str(uuid.uuid4()),
                name="王氏宗族",
                surname="王",
                hall_name="太原堂",
                origin="山西省太原市",
                description="王氏宗族起源于山西省太原市，是中国第二大姓氏。"
            )
        ]
        db.add_all(clans)
        db.commit()
        print(f"创建了 {len(clans)} 个宗族")
        
        # 3. 创建祖先数据
        ancestor_data_list = [
            AncestorData(
                id=str(uuid.uuid4()),
                user_id=users[1].id,  # 张三
                surname="张",
                hall_name="清河堂",
                ancestor_name="张公讳三",
                origin="河北省清河县",
                description="我的祖先张三，是清河堂张氏的后代，生活在清朝末年。",
                status=AncestorDataStatus.COMPLETED
            ),
            AncestorData(
                id=str(uuid.uuid4()),
                user_id=users[2].id,  # 李四
                surname="李",
                hall_name="陇西堂",
                ancestor_name="李公讳四",
                origin="甘肃省陇西县",
                description="我的祖先李四，是陇西堂李氏的后代，生活在民国时期。",
                status=AncestorDataStatus.COMPLETED
            ),
            AncestorData(
                id=str(uuid.uuid4()),
                user_id=users[3].id,  # 王五
                surname="王",
                hall_name="太原堂",
                ancestor_name="王公讳五",
                origin="山西省太原市",
                description="我的祖先王五，是太原堂王氏的后代，生活在清朝中期。",
                status=AncestorDataStatus.COMPLETED
            )
        ]
        db.add_all(ancestor_data_list)
        db.commit()
        print(f"创建了 {len(ancestor_data_list)} 条祖先数据")
        
        # 4. 创建匹配记录
        matches = [
            Match(
                id=str(uuid.uuid4()),
                ancestor_data_id=ancestor_data_list[0].id,
                clan_id=clans[0].id,  # 张氏宗族
                match_score="0.95",
                match_reasons="姓氏匹配、堂号匹配、籍贯匹配"
            ),
            Match(
                id=str(uuid.uuid4()),
                ancestor_data_id=ancestor_data_list[1].id,
                clan_id=clans[1].id,  # 李氏宗族
                match_score="0.92",
                match_reasons="姓氏匹配、堂号匹配、籍贯匹配"
            ),
            Match(
                id=str(uuid.uuid4()),
                ancestor_data_id=ancestor_data_list[2].id,
                clan_id=clans[2].id,  # 王氏宗族
                match_score="0.90",
                match_reasons="姓氏匹配、堂号匹配、籍贯匹配"
            )
        ]
        db.add_all(matches)
        db.commit()
        print(f"创建了 {len(matches)} 条匹配记录")
        
        # 5. 创建认祖申请
        applications = [
            Application(
                id=str(uuid.uuid4()),
                user_id=users[1].id,  # 张三
                ancestor_data_id=ancestor_data_list[0].id,
                clan_id=clans[0].id,  # 张氏宗族
                status=ApplicationStatus.APPROVED,
                reason="我是张氏后代，希望认祖归宗。",
                reviewed_by=users[0].id,  # 管理员
                reviewed_at=datetime.now()
            ),
            Application(
                id=str(uuid.uuid4()),
                user_id=users[2].id,  # 李四
                ancestor_data_id=ancestor_data_list[1].id,
                clan_id=clans[1].id,  # 李氏宗族
                status=ApplicationStatus.APPROVED,
                reason="我是李氏后代，希望认祖归宗。",
                reviewed_by=users[0].id,  # 管理员
                reviewed_at=datetime.now()
            ),
            Application(
                id=str(uuid.uuid4()),
                user_id=users[3].id,  # 王五
                ancestor_data_id=ancestor_data_list[2].id,
                clan_id=clans[2].id,  # 王氏宗族
                status=ApplicationStatus.APPROVED,
                reason="我是王氏后代，希望认祖归宗。",
                reviewed_by=users[0].id,  # 管理员
                reviewed_at=datetime.now()
            )
        ]
        db.add_all(applications)
        db.commit()
        print(f"创建了 {len(applications)} 条认祖申请")
        
        # 6. 更新用户的宗族信息
        users[1].clan_id = clans[0].id
        users[1].generation = "25"
        users[1].style_name = "张仁"
        users[2].clan_id = clans[1].id
        users[2].generation = "26"
        users[2].style_name = "李义"
        users[3].clan_id = clans[2].id
        users[3].generation = "24"
        users[3].style_name = "王礼"
        db.commit()
        print("更新了用户的宗族信息")
        
        # 7. 创建族谱
        genealogies = [
            Genealogy(
                id=str(uuid.uuid4()),
                name="张氏宗族族谱",
                clan_id=clans[0].id,  # 张氏宗族
                creator_id=users[0].id,  # 管理员
                description="张氏宗族的族谱，记录了家族的历史和成员信息。",
                status=GenealogyStatus.PUBLISHED,
                member_count=3
            ),
            Genealogy(
                id=str(uuid.uuid4()),
                name="李氏宗族族谱",
                clan_id=clans[1].id,  # 李氏宗族
                creator_id=users[0].id,  # 管理员
                description="李氏宗族的族谱，记录了家族的历史和成员信息。",
                status=GenealogyStatus.PUBLISHED,
                member_count=2
            )
        ]
        db.add_all(genealogies)
        db.commit()
        print(f"创建了 {len(genealogies)} 个族谱")
        
        # 8. 创建族员
        # 先创建所有族员，不设置父子关系
        genealogy_members = []
        
        # 张氏宗族族谱成员
        member1 = GenealogyMember(
            id=str(uuid.uuid4()),
            genealogy_id=genealogies[0].id,
            name="张始祖",
            gender="男",
            birth_date=datetime(1600, 1, 1),
            death_date=datetime(1680, 1, 1),
            generation="1",
            description="张氏宗族的始祖"
        )
        genealogy_members.append(member1)
        
        member2 = GenealogyMember(
            id=str(uuid.uuid4()),
            genealogy_id=genealogies[0].id,
            name="张二世",
            gender="男",
            birth_date=datetime(1630, 1, 1),
            death_date=datetime(1710, 1, 1),
            generation="2",
            description="张氏宗族的二世祖"
        )
        genealogy_members.append(member2)
        
        member3 = GenealogyMember(
            id=str(uuid.uuid4()),
            genealogy_id=genealogies[0].id,
            name="张三",
            gender="男",
            birth_date=datetime(1980, 1, 1),
            generation="25",
            description="现代张氏后代"
        )
        genealogy_members.append(member3)
        
        # 李氏宗族族谱成员
        member4 = GenealogyMember(
            id=str(uuid.uuid4()),
            genealogy_id=genealogies[1].id,
            name="李始祖",
            gender="男",
            birth_date=datetime(1550, 1, 1),
            death_date=datetime(1630, 1, 1),
            generation="1",
            description="李氏宗族的始祖"
        )
        genealogy_members.append(member4)
        
        member5 = GenealogyMember(
            id=str(uuid.uuid4()),
            genealogy_id=genealogies[1].id,
            name="李四",
            gender="男",
            birth_date=datetime(1985, 1, 1),
            generation="26",
            description="现代李氏后代"
        )
        genealogy_members.append(member5)
        db.add_all(genealogy_members)
        db.commit()
        print(f"创建了 {len(genealogy_members)} 个族员")
        
        # 更新父子关系
        member2.father_id = member1.id
        member3.father_id = member2.id
        member5.father_id = member4.id
        db.commit()
        print("更新了族员的父子关系")
        
        # 9. 创建族谱文献
        genealogy_documents = [
            GenealogyDocument(
                id=str(uuid.uuid4()),
                genealogy_id=genealogies[0].id,
                name="张氏宗族起源",
                file_path="documents/zhang_clan_origin.pdf",
                file_type="application/pdf",
                size=1024000,
                description="张氏宗族的起源和历史",
                uploaded_by=users[0].id
            ),
            GenealogyDocument(
                id=str(uuid.uuid4()),
                genealogy_id=genealogies[1].id,
                name="李氏宗族家训",
                file_path="documents/li_clan家训.txt",
                file_type="text/plain",
                size=102400,
                description="李氏宗族的家训和家规",
                uploaded_by=users[0].id
            )
        ]
        db.add_all(genealogy_documents)
        db.commit()
        print(f"创建了 {len(genealogy_documents)} 个族谱文献")
        
        # 10. 创建族谱权限
        genealogy_permissions = [
            # 给张三设置张氏族谱的查看权限
            GenealogyUserPermission(
                id=str(uuid.uuid4()),
                genealogy_id=genealogies[0].id,
                user_id=users[1].id,
                permission=GenealogyPermission.VIEW
            ),
            # 给李四设置李氏族谱的查看权限
            GenealogyUserPermission(
                id=str(uuid.uuid4()),
                genealogy_id=genealogies[1].id,
                user_id=users[2].id,
                permission=GenealogyPermission.VIEW
            )
        ]
        db.add_all(genealogy_permissions)
        db.commit()
        print(f"创建了 {len(genealogy_permissions)} 个族谱权限")
        
        # 11. 创建聊天室
        chat_rooms = [
            ChatRoom(
                id=str(uuid.uuid4()),
                name="张氏宗族聊天室",
                clan_id=clans[0].id,
                description="张氏宗族成员的交流空间"
            ),
            ChatRoom(
                id=str(uuid.uuid4()),
                name="李氏宗族聊天室",
                clan_id=clans[1].id,
                description="李氏宗族成员的交流空间"
            ),
            ChatRoom(
                id=str(uuid.uuid4()),
                name="王氏宗族聊天室",
                clan_id=clans[2].id,
                description="王氏宗族成员的交流空间"
            )
        ]
        db.add_all(chat_rooms)
        db.commit()
        print(f"创建了 {len(chat_rooms)} 个聊天室")
        
        # 12. 创建消息
        messages = [
            Message(
                id=str(uuid.uuid4()),
                chat_room_id=chat_rooms[0].id,
                user_id=users[1].id,  # 张三
                content="大家好，我是张三，很高兴加入张氏宗族！",
                message_type="text"
            ),
            Message(
                id=str(uuid.uuid4()),
                chat_room_id=chat_rooms[1].id,
                user_id=users[2].id,  # 李四
                content="大家好，我是李四，很高兴加入李氏宗族！",
                message_type="text"
            ),
            Message(
                id=str(uuid.uuid4()),
                chat_room_id=chat_rooms[2].id,
                user_id=users[3].id,  # 王五
                content="大家好，我是王五，很高兴加入王氏宗族！",
                message_type="text"
            )
        ]
        db.add_all(messages)
        db.commit()
        print(f"创建了 {len(messages)} 条消息")
        
        # 13. 创建活动
        activities = [
            Activity(
                id=str(uuid.uuid4()),
                name="张氏宗族祭祖活动",
                clan_id=clans[0].id,
                organizer_id=users[0].id,
                description="张氏宗族年度祭祖活动，欢迎所有张氏宗亲参加。",
                start_time=datetime.now() + timedelta(days=30),
                end_time=datetime.now() + timedelta(days=30, hours=4),
                location="河北省清河县张氏宗祠",
                max_participants=100,
                participant_count=10,
                status="upcoming"
            ),
            Activity(
                id=str(uuid.uuid4()),
                name="李氏宗族文化交流会",
                clan_id=clans[1].id,
                organizer_id=users[0].id,
                description="李氏宗族文化交流会，分享家族历史和文化。",
                start_time=datetime.now() + timedelta(days=60),
                end_time=datetime.now() + timedelta(days=60, hours=6),
                location="甘肃省陇西县李氏文化中心",
                max_participants=50,
                participant_count=5,
                status="upcoming"
            )
        ]
        db.add_all(activities)
        db.commit()
        print(f"创建了 {len(activities)} 个活动")
        
        # 14. 创建活动参与者
        activity_participants = [
            ActivityParticipant(
                id=str(uuid.uuid4()),
                activity_id=activities[0].id,
                user_id=users[1].id,  # 张三
                status="registered"
            ),
            ActivityParticipant(
                id=str(uuid.uuid4()),
                activity_id=activities[1].id,
                user_id=users[2].id,  # 李四
                status="registered"
            )
        ]
        db.add_all(activity_participants)
        db.commit()
        print(f"创建了 {len(activity_participants)} 个活动参与者")
        
        # 15. 创建文化分享
        culture_shares = [
            CultureShare(
                id=str(uuid.uuid4()),
                user_id=users[1].id,  # 张三
                clan_id=clans[0].id,
                title="张氏家训",
                content="张氏家训：孝悌忠信，礼义廉耻，仁爱和平。",
                likes_count=10,
                comments_count=2
            ),
            CultureShare(
                id=str(uuid.uuid4()),
                user_id=users[2].id,  # 李四
                clan_id=clans[1].id,
                title="李氏家风",
                content="李氏家风：勤奋好学，诚实守信，尊老爱幼。",
                likes_count=8,
                comments_count=1
            ),
            CultureShare(
                id=str(uuid.uuid4()),
                user_id=users[3].id,  # 王五
                clan_id=clans[2].id,
                title="王氏祖训",
                content="王氏祖训：团结互助，爱国爱家，传承文化。",
                likes_count=5,
                comments_count=0
            )
        ]
        db.add_all(culture_shares)
        db.commit()
        print(f"创建了 {len(culture_shares)} 个文化分享")
        
        # 16. 创建宗亲名片
        zongqin_cards = [
            ZongQinCard(
                id=str(uuid.uuid4()),
                user_id=users[1].id,  # 张三
                clan_id=clans[0].id,
                generation="25",
                style_name="张仁",
                introduction="张三，张氏宗族第25代传人，从事教育工作。"
            ),
            ZongQinCard(
                id=str(uuid.uuid4()),
                user_id=users[2].id,  # 李四
                clan_id=clans[1].id,
                generation="26",
                style_name="李义",
                introduction="李四，李氏宗族第26代传人，从事商业工作。"
            ),
            ZongQinCard(
                id=str(uuid.uuid4()),
                user_id=users[3].id,  # 王五
                clan_id=clans[2].id,
                generation="24",
                style_name="王礼",
                introduction="王五，王氏宗族第24代传人，从事医疗工作。"
            )
        ]
        db.add_all(zongqin_cards)
        db.commit()
        print(f"创建了 {len(zongqin_cards)} 个宗亲名片")
        
        print("数据库初始化完成！")
        
    except Exception as e:
        print(f"数据库初始化失败: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_database()
