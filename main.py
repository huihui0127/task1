序号	字段名称	说明	类型	空值说明
1	id	题目ID	str	1、不可为空
2	question_type	"题目类型，支持的类型如下：
          * singleAnswer：单选题
          * multipleAnswer：多选题
          * fillInBlank: 填空题
          * trueFalse：判断题          
          * reading：阅读题
          * cloze：完形填空
          * essay：解答题
          * listening：听力单选题
          * record：录音题/口语题
        example: singleAnswer"	str	1、空值：""
3	difficulty	题目难度，值为0-100000之间的整数	int	1、空值：-1
4	distinction	题目区分度，值为0-100000之间的整数	int	1、空值：-1
5	provider_type	"提供方类型，定义如下：
""purchase"": 供应商采购
""crawler"": 爬虫抓取
""operator"": 运营录入，""photoSearch”:拍搜"	str	1、空值：""
6	provider_id	"提供方身份信息，取值由type确定：
type=purchase时，值为供应商ID
type=crawler时，值为抓取的源网站ID
type=operator时，值为首次创建该题"	str	1、空值：""
7	question_source 	"题目来源，定义如下：
""exam"": 来源于真实考试
""selfProduced"": 自生产"	str	1、空值：""
8	choice_count	题目选项数量，对于单选题/多选题为实际选项数量；判断题选项数量为2；其它题型暂时填0	int	1、空值：-1
9	knowledge_points	题目关联的知识点ID列表，多个知识点之间使用逗号分隔	list	1、空值：[];2、类型：list
10	knowledge_name	知识点名称，用于分词索引，, 分割	str	1、空值：""
11	stem	题干，用于分词索引	str	1、空值：""
12	choices	题目选项	str	1、空值：""
13	providerkps	题目采购时关联的供应商知识点名称，多个知识点之间使用逗号分隔，用于分词索引，, 分割	str	1、空值：""
14	subject_en	题目所属学科、英文	str	1、空值：""
15	subject	题目所属学科、中文	str	1、空值：""
16	answer 	题目答案	list	1、空值：[];2、类型：list
17	interpretation	试题的解析，用于分词索引	str	1、空值：""
18	analysis_bool	是否存在解析	bool	——
19	comments	题目的总结点评，用于分词索引	str	1、空值：""
20	semester	阶段，用于分词索引	str	1、空值：""
21	semester_en	阶段、英文	str	1、空值：""
22	mediafileid	音视频托管到内容平台上的原生id，可通过此id从wisecontent获取到原生音视频访问地址	list	1、空值：[];2、类型：list
23	file_content	"音频文本
1、仅针口语题，采购题目时不管是否有口语音频，会同时将口语文本传入，一般不超过512字符（1-5句话）
2、针对听力题，采购题目时有听力音频，暂无需将音频文本传入
注：单个文本中可能有逗号等符号，2个口语文本分隔时，需要屏蔽逗号的影响，避免数据无法拆分读取。"	list	1、空值：[];2、类型：list
24	sub_questions	子题目id列表，id列表顺序为用户端/管理展示顺序	list	1、空值：[];2、类型：list
25	listing_status	"上架状态，
生效情况（0-未生效 1-生效中 2-失效中）"	int	1、空值：-1
26	review_status	"审核状态，
表示题目在生命周期内审核状态变更。（2,新建待审核 3,新建审核通过 4,新建审核驳回 6, 更新待审核 7, 更新审核通过 8, 更新审核驳回 12,失效待审核 13,失效审核通过 14,失效不通过）"	int	1、空值：-1
27	question_label 	"题目标签。
question - 题目（大题，完整1道题）；
sub-question - 子题（依赖大题，不能单独存在）"	str	1、空值：""
28	purpose	"题目用途
assessment -- 测评
photoSearch  --拍搜"	list	1、空值：[];2、类型：list
29	solution	题目的完整解答过程，支持HTML+LaTex格式的内容	str	1、空值：""
30	knowledge_weight	知识点权重	list	1、空值：[];2、类型：list
31	reviewer	审核人,多个审核人按先后顺序排序	list	1、空值：[];2、类型：list
32	img_url	图片链接地址	dict	1、空值：{}
33	stem_img_bool	题干是否存在图片	enum	false/true
34	resourceChildKPName	用于分词索引，,分割	str	1、空值：""
35	grade	年级、中文	str	1、空值：""
36	grade_id	年级	str	1、空值：""
37	img_media_id	图片的media ID，用于内网下载	dict	1、空值：{}
38	img_file_id	图片的file ID，用于内网下载	dict	1、空值：{}
39	un_normal_id	记录内网下载的ID，区别与普通可下载链接	list	1、空值：[]
40	fallible	是否易错题	enum	0/1
41	finale	是否压轴题	enum	0/1
42	frequentlyused	是否常考题	enum	0/1
43	highquality	是否好题	enum	0/1
44	examname	考试名称	str	1、空值：null
45	examtype_en	"考试类型,英文名称
'exercise: 课后习题
entrance: 开学考试
unit: 单元测试
monthly: 月考
midTerm: 期中考试
final: 期末考试
joint: 联考
mock: 模拟考试
survey: 调研考试
middleSchoolEntrance: 小升初考试
highSchoolEntrance: 中考
collegeEntrance：高考
other: 其它"	enum	1、空值：other
46	examyear	考试年份,	int	1、空值：null
47	region	考试地区, 	list	1、空值：[]
