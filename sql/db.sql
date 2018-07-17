CREATE TABLE `author` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `aname` varchar(100) DEFAULT '' COMMENT '姓名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3433 DEFAULT CHARSET=utf8

CREATE TABLE `author_link` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `author_id` bigint(20) DEFAULT NULL COMMENT 'author.id',
  `site_id` int(4) DEFAULT NULL COMMENT '网站id',
  `url` varchar(500) DEFAULT '' COMMENT '网址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18486 DEFAULT CHARSET=utf8


CREATE TABLE `site` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `sname` varchar(100) DEFAULT '' COMMENT '站点名',
  `url` varchar(1000) DEFAULT '' COMMENT '站点网址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8


CREATE TABLE `song` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `sname` varchar(100) DEFAULT '' COMMENT '姓名',
  `author_id` bigint(20) DEFAULT '0' COMMENT '作者author.id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14889 DEFAULT CHARSET=utf8


CREATE TABLE `tab` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `song_id` bigint(20) DEFAULT NULL COMMENT 'song.id',
  `url` varchar(1000) DEFAULT '' COMMENT '来源网址',
  `site_id` bigint(20) DEFAULT '0' COMMENT 'site.id',
  `ttype` tinyint(1) DEFAULT '0' COMMENT '0 未知 1文本 2 图片 3 gtp 4 html',
  `content` mediumtext COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19961 DEFAULT CHARSET=utf8