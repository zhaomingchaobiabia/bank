/*
SQLyog Professional v10.51 
MySQL - 5.7.26-log : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$150000$epjRjqwkPlBD$G6UsmYGM7V6vwu3tA8wvllqeDFU10hN11ZjlwWMeQto=','2019-08-30 11:24:12.778983',1,'zhuningning','','','zhuningning@git.com',1,1,'2019-08-30 11:18:35.500001');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2019-08-26 15:43:54.557676'),(2,'auth','0001_initial','2019-08-26 15:43:56.322063'),(3,'admin','0001_initial','2019-08-26 15:44:03.306385'),(4,'admin','0002_logentry_remove_auto_add','2019-08-26 15:44:04.816687'),(5,'admin','0003_logentry_add_action_flag_choices','2019-08-26 15:44:04.892713'),(6,'contenttypes','0002_remove_content_type_name','2019-08-26 15:44:06.005722'),(7,'auth','0002_alter_permission_name_max_length','2019-08-26 15:44:06.888916'),(8,'auth','0003_alter_user_email_max_length','2019-08-26 15:44:07.695215'),(9,'auth','0004_alter_user_username_opts','2019-08-26 15:44:07.758224'),(10,'auth','0005_alter_user_last_login_null','2019-08-26 15:44:08.513250'),(11,'auth','0006_require_contenttypes_0002','2019-08-26 15:44:08.580276'),(12,'auth','0007_alter_validators_add_error_messages','2019-08-26 15:44:08.652274'),(13,'auth','0008_alter_user_username_max_length','2019-08-26 15:44:09.403327'),(14,'auth','0009_alter_user_last_name_max_length','2019-08-26 15:44:10.053397'),(15,'auth','0010_alter_group_name_max_length','2019-08-26 15:44:10.737578'),(16,'auth','0011_update_proxy_permissions','2019-08-26 15:44:10.821575'),(17,'sessions','0001_initial','2019-08-26 15:44:11.151573');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('0y6i1ck4lrtkyd2pq7jrzggliwjaqgf4','NDRmM2YwMWE4MzY3MTM1NTFiODRmNTRjMjgzZjMwNjMyNmM1ZDBjMjp7ImxvZ2luIjp7ImlkIjoyLCJ0ZWwiOiIxMjU0Nzg0NTY5OCJ9fQ==','2019-09-12 02:21:20.386765'),('afzs75h3pte21p8u7cvpeklhirwvexkw','NDgxNDNiMmFkNDM1MmM2ODczZDJlNGQyMGRkM2M3ZDEwNDFlMmJmODp7ImxvZ2luRmxhZyI6eyJpZCI6MjIsInRlbCI6IjE1NjUwNTU2MzYyIn0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-11 21:21:17.124817'),('cbcu4uxk6sdz1dh1k8o7m5er7dbwsck7','MTc4Njk4ZjM3Zjg5OGViOWI2YWRhNWY1ZWY4MzAxZDY2NzIwMGU5ZTp7ImxvZ2luIjp7ImlkIjozLCJ0ZWwiOiIyMzEzMTEzMjEzMSJ9fQ==','2019-09-12 02:11:15.303920'),('chano6gg7x43gp15gd2mjpmmbq3unw6b','MTc4Njk4ZjM3Zjg5OGViOWI2YWRhNWY1ZWY4MzAxZDY2NzIwMGU5ZTp7ImxvZ2luIjp7ImlkIjozLCJ0ZWwiOiIyMzEzMTEzMjEzMSJ9fQ==','2019-09-12 02:30:04.186306'),('dxordxgpn2lrcn7rir8e6sb3c06jttbg','ZWI4MmU1NjU2MWUzYzVkODJhZTQ0MDNjMjExMTdlNjg3NDM0YTI2ZDp7ImxvZ2luRmxhZyI6eyJpZCI6MjAsInRlbCI6IjEzMTU0MjExMjEyIn0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-11 20:44:13.823293'),('h5788yu4q3rjmk4lzrmd6fe3k7rq31zz','ZWQ2NGViMTVkZDkwYWU2ODNlNDBkZWI2NWUyZmYyZTYyNDYwYzk1NDp7ImxvZ2luRmxhZyI6eyJpZCI6MTksInRlbCI6IjE1NDc5NTYyMTU2In0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-12 22:00:13.693800'),('nnhxy9afftrznn64f75eg2xwuxd0ukua','ZWQ2NGViMTVkZDkwYWU2ODNlNDBkZWI2NWUyZmYyZTYyNDYwYzk1NDp7ImxvZ2luRmxhZyI6eyJpZCI6MTksInRlbCI6IjE1NDc5NTYyMTU2In0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-13 19:23:55.949877'),('ql7wyr5kv8blvycmr242zx5nxtv0v9s0','ZWQ2NGViMTVkZDkwYWU2ODNlNDBkZWI2NWUyZmYyZTYyNDYwYzk1NDp7ImxvZ2luRmxhZyI6eyJpZCI6MTksInRlbCI6IjE1NDc5NTYyMTU2In0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-13 19:31:13.166431'),('rcyhnxu5fbvjay6jtee25x5i4assgo0t','NDRmM2YwMWE4MzY3MTM1NTFiODRmNTRjMjgzZjMwNjMyNmM1ZDBjMjp7ImxvZ2luIjp7ImlkIjoyLCJ0ZWwiOiIxMjU0Nzg0NTY5OCJ9fQ==','2019-09-12 07:08:19.431537'),('v3mihivhw1bnpuvfxxuzrbbgtgzvtt7q','OTQwOWVjYWZmNzZhZWRmZGVhMzgyYmIxMTExNzEzM2MzNWEyMmRkZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NTU0ZTIzMjY5NTMxNzhlYmM4ZTA4NjljNmRjMzA2ZTMxMzZkMDhhIn0=','2019-09-13 11:24:12.838971'),('viwnel9pcrglzauutytq4q0dix3gojnb','NDgxNDNiMmFkNDM1MmM2ODczZDJlNGQyMGRkM2M3ZDEwNDFlMmJmODp7ImxvZ2luRmxhZyI6eyJpZCI6MjIsInRlbCI6IjE1NjUwNTU2MzYyIn0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-13 17:49:12.106447'),('xea54jle3epk6eyr93u2jda4iccor94x','ZWQ2NGViMTVkZDkwYWU2ODNlNDBkZWI2NWUyZmYyZTYyNDYwYzk1NDp7ImxvZ2luRmxhZyI6eyJpZCI6MTksInRlbCI6IjE1NDc5NTYyMTU2In0sIl9zZXNzaW9uX2V4cGlyeSI6MH0=','2019-09-12 11:27:40.340548');

/*Table structure for table `money_record` */

DROP TABLE IF EXISTS `money_record`;

CREATE TABLE `money_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL COMMENT '用户id',
  `money` int(11) DEFAULT NULL COMMENT '金额',
  `from_src` varchar(100) DEFAULT NULL COMMENT '金额来源',
  `change_time` datetime DEFAULT NULL COMMENT '交易时间',
  `banlence` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `money_record_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_user_info` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8;

/*Data for the table `money_record` */

insert  into `money_record`(`id`,`user_id`,`money`,`from_src`,`change_time`,`banlence`) values (129,19,10000000,'用户充值','2019-08-28 20:09:22',10000000),(130,19,10000,'投资','2019-08-28 20:10:53',0),(131,20,100000000,'用户充值','2019-08-28 20:16:06',100000000),(132,21,0,'余额不足，还款失败','2019-08-28 20:24:56',NULL),(133,19,11111,'投资','2019-08-28 20:47:54',9990000),(134,19,50,'投资','2019-08-28 20:48:35',9978890),(135,19,840,'投资','2019-08-28 20:50:55',9978000),(136,22,0,'余额不足，还款失败','2019-08-28 21:11:43',NULL),(137,22,21,'用户充值','2019-08-28 21:11:49',21),(138,22,21,'还款','2019-08-28 21:12:05',NULL),(139,22,1000,'用户充值','2019-08-29 09:48:58',1000),(140,22,1000,'投资','2019-08-29 09:53:01',0),(141,25,100000,'用户充值','2019-08-29 10:19:40',100000),(142,25,10000,'投资','2019-08-29 10:20:05',90000),(143,19,5000,'用户充值','2019-08-29 10:24:35',9983000),(144,19,8000,'用户充值','2019-08-29 10:24:40',9991000),(145,22,100,'用户充值','2019-08-30 17:17:10',100),(146,22,100,'投资','2019-08-30 17:17:30',0),(147,22,1,'用户充值','2019-08-30 17:17:41',1),(148,22,1,'用户充值','2019-08-30 17:17:48',2),(149,22,100,'用户充值','2019-08-30 17:29:55',102),(150,22,100,'投资','2019-08-30 17:30:09',2),(151,22,100,'用户充值','2019-08-30 17:34:20',102),(152,22,100,'投资','2019-08-30 17:35:24',2),(153,22,10000,'用户充值','2019-08-30 17:37:03',10002),(154,22,100,'投资','2019-08-30 17:37:15',9902),(155,22,100,'投资','2019-08-30 17:38:18',9802),(156,22,100,'投资','2019-08-30 17:40:04',9702),(157,22,100,'投资','2019-08-30 17:41:57',9602),(158,22,100,'投资','2019-08-30 17:44:19',9502),(159,22,1,'投资','2019-08-30 17:49:09',9501);

/*Table structure for table `payment_history` */

DROP TABLE IF EXISTS `payment_history`;

CREATE TABLE `payment_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL COMMENT '应还款用户id',
  `project_id` int(11) DEFAULT NULL COMMENT '应还款项目id',
  `money` int(11) DEFAULT NULL COMMENT '本月应还金额',
  `repay_time` datetime DEFAULT NULL COMMENT '还款时间',
  `balance` int(11) DEFAULT NULL COMMENT '本月还款月',
  `status` varchar(10) DEFAULT NULL COMMENT '还款状态',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `payment_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_user_info` (`ID`),
  CONSTRAINT `payment_history_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project_list` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `payment_history` */

insert  into `payment_history`(`id`,`user_id`,`project_id`,`money`,`repay_time`,`balance`,`status`) values (3,21,31,100,'2019-08-15 19:28:52',20,'未还款'),(4,22,31,500,'2019-08-15 20:01:52',60,'未还款');

/*Table structure for table `project_invest` */

DROP TABLE IF EXISTS `project_invest`;

CREATE TABLE `project_invest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL COMMENT '投资项目id',
  `user_id` int(11) DEFAULT NULL COMMENT '投资人用户id',
  `money` int(11) DEFAULT NULL COMMENT '投资金额',
  `invest_time` datetime DEFAULT NULL COMMENT '投资时间',
  `pay_time` datetime DEFAULT NULL COMMENT '收益产生时间',
  `note` varchar(500) DEFAULT NULL COMMENT '投资备注信息',
  `get_money` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `project_invest_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_user_info` (`ID`),
  CONSTRAINT `project_invest_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project_list` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

/*Data for the table `project_invest` */

insert  into `project_invest`(`id`,`project_id`,`user_id`,`money`,`invest_time`,`pay_time`,`note`,`get_money`) values (16,31,22,800,'2019-08-30 17:44:19',NULL,NULL,NULL);

/*Table structure for table `project_list` */

DROP TABLE IF EXISTS `project_list`;

CREATE TABLE `project_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(20) DEFAULT NULL COMMENT '项目名称',
  `tel` varchar(11) DEFAULT NULL COMMENT '申请人',
  `loan_type` varchar(20) DEFAULT NULL COMMENT '信用类型',
  `money` int(11) DEFAULT NULL COMMENT '贷款总金额',
  `loan` int(11) DEFAULT NULL COMMENT '借款期限——单位月',
  `rate` int(11) DEFAULT NULL COMMENT '年利率——单位%',
  `loanuse` varchar(50) DEFAULT NULL COMMENT '借款用途',
  `min_money` int(11) DEFAULT NULL COMMENT '最低投标金额',
  `max_money` int(11) DEFAULT NULL COMMENT '最高投标金额',
  `valid_time` int(11) DEFAULT NULL COMMENT '单位——天',
  `repay_type` varchar(11) DEFAULT NULL COMMENT '还款方式',
  `status` varchar(10) DEFAULT NULL COMMENT '项目状态',
  `project_password` varchar(32) DEFAULT NULL,
  `get_money` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

/*Data for the table `project_list` */

insert  into `project_list`(`id`,`project_name`,`tel`,`loan_type`,`money`,`loan`,`rate`,`loanuse`,`min_money`,`max_money`,`valid_time`,`repay_type`,`status`,`project_password`,`get_money`,`time`) values (31,'河南省保护少女儿童项目投资','朱宁宁','担保',100,12,12,'短期周转',10000,100000,7,'先息后本','已完成','666666',100,'2019-08-29 21:21:04'),(32,'111','11','1',1,1,1,'1',1,1,1,'1','已完成','666666',1,'2019-08-02 17:39:28');

/*Table structure for table `t_back_user_info` */

DROP TABLE IF EXISTS `t_back_user_info`;

CREATE TABLE `t_back_user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tel` varchar(11) DEFAULT NULL COMMENT '联系方式',
  `password` varchar(32) DEFAULT NULL COMMENT '密码',
  `realname` varchar(50) DEFAULT NULL COMMENT '真实姓名',
  `username` varchar(500) DEFAULT NULL COMMENT '用户名',
  `email` varchar(100) DEFAULT NULL COMMENT '企业邮箱',
  `birthday` date DEFAULT NULL COMMENT '出生日期',
  `address` varchar(500) DEFAULT NULL COMMENT '现居地址',
  `jobtime` datetime DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL COMMENT '用户头像',
  `SEX` varchar(6) DEFAULT NULL,
  `card` varchar(18) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `t_back_user_info` */

insert  into `t_back_user_info`(`id`,`tel`,`password`,`realname`,`username`,`email`,`birthday`,`address`,`jobtime`,`photo`,`SEX`,`card`) values (2,'12547845698','111','小哦下','消息i奥','23131@','1994-04-01','郑州','2019-08-09 00:00:00',NULL,'女','412154784785445698'),(3,'23131132131','111','大撒','达到3','阿萨大大','1993-08-25','河南','2019-08-02 00:00:00',NULL,'男','412154784512445698'),(4,'15650556362','111','李衍文','六六','111@git.com','2019-08-23','山东','2019-08-01 00:00:00',NULL,'男','412154784512445698');

/*Table structure for table `t_borrow_info` */

DROP TABLE IF EXISTS `t_borrow_info`;

CREATE TABLE `t_borrow_info` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `REALNAME` varchar(50) DEFAULT NULL COMMENT '申请人',
  `TEL` varchar(11) DEFAULT NULL COMMENT '手机号',
  `REGION` varchar(50) DEFAULT NULL COMMENT '所属地区',
  `MONEY` int(11) DEFAULT NULL COMMENT '借款金额',
  `LOAN` int(11) DEFAULT NULL COMMENT '借款期限',
  `LOANTYPE` varchar(50) DEFAULT NULL COMMENT '借款方式',
  `LOANUSE` varchar(50) DEFAULT NULL COMMENT '借款用途',
  `status` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `t_borrow_info_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_user_info` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;

/*Data for the table `t_borrow_info` */

insert  into `t_borrow_info`(`ID`,`REALNAME`,`TEL`,`REGION`,`MONEY`,`LOAN`,`LOANTYPE`,`LOANUSE`,`status`,`user_id`,`time`) values (90,'李衍文','15650556362','河南省郑州市',1000000,24,'信用','短期周转','申请中',22,'2019-08-30 11:04:52');

/*Table structure for table `t_login_info` */

DROP TABLE IF EXISTS `t_login_info`;

CREATE TABLE `t_login_info` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `IP` varchar(100) DEFAULT NULL COMMENT '登录IP地址',
  `LOGINTIME` date DEFAULT NULL COMMENT '登录时间',
  PRIMARY KEY (`ID`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `t_login_info_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `t_user_info` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `t_login_info` */

/*Table structure for table `t_role` */

DROP TABLE IF EXISTS `t_role`;

CREATE TABLE `t_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rolename` varchar(11) DEFAULT NULL COMMENT '角色名',
  `roledesc` varchar(32) DEFAULT NULL COMMENT '角色描述',
  `status` int(11) DEFAULT NULL COMMENT '状态 -1代表失效',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `t_role` */

/*Table structure for table `t_role_perm` */

DROP TABLE IF EXISTS `t_role_perm`;

CREATE TABLE `t_role_perm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) DEFAULT NULL,
  `modname` varchar(100) DEFAULT NULL COMMENT '菜单名',
  PRIMARY KEY (`id`),
  KEY `t_fr_roleid` (`role_id`),
  CONSTRAINT `t_fr_roleid` FOREIGN KEY (`role_id`) REFERENCES `t_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `t_role_perm` */

/*Table structure for table `t_user_info` */

DROP TABLE IF EXISTS `t_user_info`;

CREATE TABLE `t_user_info` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TEL` varchar(11) DEFAULT NULL COMMENT '联系方式/账号',
  `PASSWORD` varchar(32) DEFAULT NULL COMMENT '密码',
  `REALNAME` varchar(50) DEFAULT NULL COMMENT '真实姓名',
  `POSTCARD` varchar(18) DEFAULT NULL COMMENT '身份证',
  `BANLENCE` float DEFAULT NULL COMMENT '账户余额',
  `PAY` varchar(32) DEFAULT '111' COMMENT '支付密码',
  `IMG` varchar(100) DEFAULT NULL COMMENT '用户头像',
  `CREATETIME` date DEFAULT NULL COMMENT '注册时间',
  `flag` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

/*Data for the table `t_user_info` */

insert  into `t_user_info`(`ID`,`TEL`,`PASSWORD`,`REALNAME`,`POSTCARD`,`BANLENCE`,`PAY`,`IMG`,`CREATETIME`,`flag`) values (19,'15479562156','7fa8282ad93047a4d6fe6111c93b308a','大大','123123212354642311',9991000,'111','',NULL,1),(20,'13154211212','96e79218965eb72c92a549dd5a330112','图片','121131211111111123',100000000,'111','',NULL,1),(21,'18239436825','23a3bd9f93a6826cde8ebde68853ba83','朱宁宁','412728445578994546',100,'111','',NULL,1),(22,'15650556362','7fa8282ad93047a4d6fe6111c93b308a','李衍文','',9501,'111','',NULL,1),(25,'15650556363','7fa8282ad93047a4d6fe6111c93b308a','','',90000,'111','',NULL,1),(26,'15650556364','7fa8282ad93047a4d6fe6111c93b308a','lilili','111111111111111111',0,'111','',NULL,1);

/*Table structure for table `t_user_role` */

DROP TABLE IF EXISTS `t_user_role`;

CREATE TABLE `t_user_role` (
  `role_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`role_id`,`user_id`),
  KEY `t_f_roledesc` (`user_id`),
  CONSTRAINT `t_f_roledesc` FOREIGN KEY (`user_id`) REFERENCES `t_back_user_info` (`id`),
  CONSTRAINT `t_f_roleid` FOREIGN KEY (`role_id`) REFERENCES `t_role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `t_user_role` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
