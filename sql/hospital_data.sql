/*
 Navicat Premium Dump SQL

 Source Server         : p5003
 Source Server Type    : MySQL
 Source Server Version : 80407 (8.4.7)
 Source Host           : localhost:3306
 Source Schema         : hospital

 Target Server Type    : MySQL
 Target Server Version : 80407 (8.4.7)
 File Encoding         : 65001

 Date: 10/12/2025 21:53:31
*/
DROP DATABASE IF EXISTS hospital;
CREATE DATABASE hospital CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

-- 第二步：显式地选择数据库
USE hospital;
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for department
-- ----------------------------
DROP TABLE IF EXISTS `department`;
CREATE TABLE `department`  (
  `dept_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '科室编号',
  `dept_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '科室名称',
  `location` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '位置',
  `staff_count` int NULL DEFAULT 0 COMMENT '科室人数',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`dept_id`) USING BTREE,
  INDEX `idx_dept_name`(`dept_name` ASC) USING BTREE,
  INDEX `idx_dept_location`(`location` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '科室表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of department
-- ----------------------------
INSERT INTO `department` VALUES ('1111', 'd', 'f', 22, '2025-12-10 03:06:12', '2025-12-10 03:06:12');
INSERT INTO `department` VALUES ('176535561238999293', 'd1', '2f', 10, '2025-12-10 16:33:32', '2025-12-10 16:33:32');
INSERT INTO `department` VALUES ('176535562009041452', 'd2', '2f', 20, '2025-12-10 16:33:40', '2025-12-10 16:33:40');
INSERT INTO `department` VALUES ('8989', 'abc', 'aa', 2, '2025-12-10 03:05:47', '2025-12-10 03:05:47');

-- ----------------------------
-- Table structure for diagnosis
-- ----------------------------
DROP TABLE IF EXISTS `diagnosis`;
CREATE TABLE `diagnosis`  (
  `diagnosis_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '诊断记录编号',
  `registration_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '挂号单号',
  `doctor_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '医生ID',
  `diagnosis_time` datetime NOT NULL COMMENT '诊断时间',
  `diagnosis_note` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '诊断说明',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`diagnosis_id`) USING BTREE,
  INDEX `idx_diagnosis_registration`(`registration_id` ASC) USING BTREE,
  INDEX `idx_diagnosis_doctor`(`doctor_id` ASC) USING BTREE,
  INDEX `idx_diagnosis_time`(`diagnosis_time` ASC) USING BTREE,
  INDEX `idx_diagnosis_doctor_time`(`doctor_id` ASC, `diagnosis_time` ASC) USING BTREE,
  CONSTRAINT `fk_diagnosis_doctor` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_diagnosis_registration` FOREIGN KEY (`registration_id`) REFERENCES `registration` (`registration_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '诊断记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of diagnosis
-- ----------------------------
INSERT INTO `diagnosis` VALUES ('176536129471065358', '176535792246732856', '176535580122376349', '2025-12-10 10:07:06', 'test1', '2025-12-10 18:08:14', '2025-12-10 18:08:14');

-- ----------------------------
-- Table structure for doctor
-- ----------------------------
DROP TABLE IF EXISTS `doctor`;
CREATE TABLE `doctor`  (
  `doctor_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '医生ID',
  `doctor_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '医生姓名',
  `title` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '职称',
  `gender` enum('M','F') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '性别: M-男, F-女',
  `age` int NOT NULL COMMENT '年龄',
  `experience` int NULL DEFAULT 0 COMMENT '工作经验(年)',
  `salary` decimal(10, 2) NULL DEFAULT 0.00 COMMENT '工资',
  `dept_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '科室编号',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`doctor_id`) USING BTREE,
  INDEX `idx_doctor_dept`(`dept_id` ASC) USING BTREE,
  INDEX `idx_doctor_gender`(`gender` ASC) USING BTREE,
  INDEX `idx_doctor_title`(`title` ASC) USING BTREE,
  INDEX `idx_doctor_name`(`doctor_name` ASC) USING BTREE,
  INDEX `idx_doctor_age`(`age` ASC) USING BTREE,
  INDEX `idx_doctor_experience`(`experience` ASC) USING BTREE,
  CONSTRAINT `fk_doctor_dept` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '医生表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of doctor
-- ----------------------------
INSERT INTO `doctor` VALUES ('176535579022423331', 't1', 'string', 'M', 30, 0, 10.00, '1111', '2025-12-10 16:36:30', '2025-12-10 16:36:30');
INSERT INTO `doctor` VALUES ('176535580122376349', 't2', 'string', 'M', 40, 20, 120.00, '1111', '2025-12-10 16:36:41', '2025-12-10 16:36:41');

-- ----------------------------
-- Table structure for garage
-- ----------------------------
DROP TABLE IF EXISTS `garage`;
CREATE TABLE `garage`  (
  `garage_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '车库编号',
  `is_full` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否满位: 0-未满, 1-满位',
  `area` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '车库区域(如A区、B区)',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`garage_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '车库表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of garage
-- ----------------------------

-- ----------------------------
-- Table structure for medicine
-- ----------------------------
DROP TABLE IF EXISTS `medicine`;
CREATE TABLE `medicine`  (
  `medicine_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药品编号',
  `medicine_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药品名称',
  `quantity` int NOT NULL DEFAULT 0 COMMENT '库存数量',
  `is_otc` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否非处方药: 0-否, 1-是',
  `production_date` date NOT NULL COMMENT '生产日期',
  `expiration_date` date NOT NULL COMMENT '过期日期',
  `indications` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '药品适用范围',
  `price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '价格',
  `factory_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '药厂编号',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`medicine_id`) USING BTREE,
  INDEX `idx_medicine_name`(`medicine_name` ASC) USING BTREE,
  INDEX `idx_medicine_quantity`(`quantity` ASC) USING BTREE,
  INDEX `idx_medicine_is_otc`(`is_otc` ASC) USING BTREE,
  INDEX `idx_medicine_price`(`price` ASC) USING BTREE,
  INDEX `idx_medicine_expiration`(`expiration_date` ASC) USING BTREE,
  INDEX `idx_medicine_production_date`(`production_date` ASC) USING BTREE,
  INDEX `idx_medicine_stock_status`(`quantity` ASC, `expiration_date` ASC) USING BTREE,
  INDEX `idx_medicine_factory`(`factory_id` ASC) USING BTREE,
  CONSTRAINT `fk_medicine_factory` FOREIGN KEY (`factory_id`) REFERENCES `pharmaceutical_factory` (`pharmaceutical_factory`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '药品库存表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of medicine
-- ----------------------------
INSERT INTO `medicine` VALUES ('176535444763621655', 'ss', 10, 1, '2025-12-10', '2028-12-10', 'ss', 20.00, '176535416287028261', '2025-12-10 16:14:07', '2025-12-10 21:52:46');
INSERT INTO `medicine` VALUES ('176535450419977608', 'ss', 5, 1, '2025-12-10', '2027-12-10', 'ss', 20.00, '176535416287028261', '2025-12-10 16:15:04', '2025-12-10 16:15:04');
INSERT INTO `medicine` VALUES ('a7', 'string', 20, 1, '2025-12-10', '2025-12-10', 'se', 0.00, 'f123', '2025-12-10 03:36:44', '2025-12-10 16:41:21');
INSERT INTO `medicine` VALUES ('a8', 'a7', 7, 1, '2025-12-09', '2035-12-09', 'string', 5.00, 'f123', '2025-12-10 03:37:31', '2025-12-10 03:37:31');

-- ----------------------------
-- Table structure for parking
-- ----------------------------
DROP TABLE IF EXISTS `parking`;
CREATE TABLE `parking`  (
  `parking_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '停车记录ID',
  `car_no` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '车牌号',
  `garage_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '关联车库编号',
  `patient_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '关联患者编号',
  `in_time` datetime NOT NULL COMMENT '入场时间',
  `out_time` datetime NULL DEFAULT NULL COMMENT '出场时间',
  `fee` decimal(10, 2) NULL DEFAULT NULL COMMENT '停车费用',
  `car_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '车辆类型',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`parking_id`) USING BTREE,
  INDEX `idx_parking_garage`(`garage_id` ASC) USING BTREE,
  INDEX `idx_parking_patient`(`patient_id` ASC) USING BTREE,
  CONSTRAINT `fk_parking_garage` FOREIGN KEY (`garage_id`) REFERENCES `garage` (`garage_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `fk_parking_patient` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '停车记录表' ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of parking
-- ----------------------------

-- ----------------------------
-- Table structure for patient
-- ----------------------------
DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient`  (
  `patient_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '患者ID',
  `patient_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '患者姓名',
  `age` int NOT NULL COMMENT '年龄',
  `gender` enum('M','F') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '性别: M-男, F-女',
  `height` decimal(5, 2) NULL DEFAULT NULL COMMENT '身高(cm)',
  `weight` decimal(5, 2) NULL DEFAULT NULL COMMENT '体重(kg)',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`patient_id`) USING BTREE,
  INDEX `idx_patient_gender`(`gender` ASC) USING BTREE,
  INDEX `idx_patient_age`(`age` ASC) USING BTREE,
  INDEX `idx_patient_name`(`patient_name` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '患者表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of patient
-- ----------------------------
INSERT INTO `patient` VALUES ('176535617536843533', 'p1', 10, 'M', 120.00, 120.00, '2025-12-10 16:42:55', '2025-12-10 16:42:55');
INSERT INTO `patient` VALUES ('176535620112394425', 'p1', 110, 'F', 10.00, 120.00, '2025-12-10 16:43:21', '2025-12-10 16:43:21');

-- ----------------------------
-- Table structure for pharmaceutical_factory
-- ----------------------------
DROP TABLE IF EXISTS `pharmaceutical_factory`;
CREATE TABLE `pharmaceutical_factory`  (
  `factory_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药厂编号',
  `factory_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '厂名',
  `manager` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '总经理',
  `address` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '地址',
  `qualification_level` int NOT NULL COMMENT '资格证等级',
  `phone_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药厂电话',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`factory_id`) USING BTREE,
  INDEX `idx_factory_name`(`factory_name` ASC) USING BTREE,
  INDEX `idx_factory_qualification`(`qualification_level` ASC) USING BTREE,
  INDEX `idx_factory_phone`(`phone_number` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '药厂表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pharmaceutical_factory
-- ----------------------------
INSERT INTO `pharmaceutical_factory` VALUES ('176535415072490149', '666', '66', 'w6', 1, '88', '2025-12-10 16:09:10', '2025-12-10 16:09:10');
INSERT INTO `pharmaceutical_factory` VALUES ('176535416287028261', '777', '7', 'w7', 3, '88', '2025-12-10 16:09:22', '2025-12-10 16:09:22');
INSERT INTO `pharmaceutical_factory` VALUES ('f123', 't1', 'tt', 'ttt', 5, '123', '2025-12-10 03:36:21', '2025-12-10 03:36:21');

-- ----------------------------
-- Table structure for prescription
-- ----------------------------
DROP TABLE IF EXISTS `prescription`;
CREATE TABLE `prescription`  (
  `prescription_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '取药单号',
  `treatment_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '治疗单号',
  `medicine_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药品编号',
  `patient_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '患者ID',
  `price` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '价格',
  `quantity` int NOT NULL DEFAULT 1 COMMENT '取药数量',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`prescription_id`) USING BTREE,
  INDEX `idx_prescription_patient`(`patient_id` ASC) USING BTREE,
  INDEX `idx_prescription_medicine`(`medicine_id` ASC) USING BTREE,
  INDEX `idx_prescription_treatment`(`treatment_id` ASC) USING BTREE,
  INDEX `idx_prescription_price`(`price` ASC) USING BTREE,
  INDEX `idx_prescription_patient_medicine`(`patient_id` ASC, `medicine_id` ASC) USING BTREE,
  INDEX `idx_prescription_patient_time`(`patient_id` ASC, `created_at` ASC) USING BTREE,
  INDEX `idx_prescription_covering`(`patient_id` ASC, `medicine_id` ASC, `price` ASC, `prescription_id` ASC) USING BTREE,
  CONSTRAINT `fk_prescription_medicine` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`medicine_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_prescription_patient` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_prescription_treatment` FOREIGN KEY (`treatment_id`) REFERENCES `treatment` (`treatment_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '取药单表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of prescription
-- ----------------------------

-- ----------------------------
-- Table structure for registration
-- ----------------------------
DROP TABLE IF EXISTS `registration`;
CREATE TABLE `registration`  (
  `registration_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '挂号单号',
  `window_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '窗口编号',
  `patient_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '患者ID',
  `doctor_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '医生ID',
  `registration_time` datetime NOT NULL COMMENT '挂号时间',
  `fee` decimal(10, 2) NOT NULL DEFAULT 0.00 COMMENT '挂号费用',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`registration_id`) USING BTREE,
  INDEX `idx_registration_patient`(`patient_id` ASC) USING BTREE,
  INDEX `idx_registration_doctor`(`doctor_id` ASC) USING BTREE,
  INDEX `idx_registration_window`(`window_id` ASC) USING BTREE,
  INDEX `idx_registration_time`(`registration_time` ASC) USING BTREE,
  INDEX `idx_registration_fee`(`fee` ASC) USING BTREE,
  INDEX `idx_registration_patient_time`(`patient_id` ASC, `registration_time` ASC) USING BTREE,
  INDEX `idx_registration_doctor_time`(`doctor_id` ASC, `registration_time` ASC) USING BTREE,
  CONSTRAINT `fk_registration_doctor` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_registration_patient` FOREIGN KEY (`patient_id`) REFERENCES `patient` (`patient_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_registration_window` FOREIGN KEY (`window_id`) REFERENCES `registration_window` (`window_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '挂号表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of registration
-- ----------------------------
INSERT INTO `registration` VALUES ('176535792246732856', '176535674200979472', '176535617536843533', '176535580122376349', '2025-12-10 08:48:43', 110.00, '2025-12-10 17:12:02', '2025-12-10 17:45:00');
INSERT INTO `registration` VALUES ('176535843049755383', '176535674200979472', '176535617536843533', '176535580122376349', '2025-12-10 08:48:45', 0.00, '2025-12-10 17:20:30', '2025-12-10 17:20:30');

-- ----------------------------
-- Table structure for registration_window
-- ----------------------------
DROP TABLE IF EXISTS `registration_window`;
CREATE TABLE `registration_window`  (
  `window_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '窗口编号',
  `doctor_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '医生ID',
  `waiting_count` int NULL DEFAULT 0 COMMENT '等待人数',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`window_id`) USING BTREE,
  INDEX `idx_window_doctor`(`doctor_id` ASC) USING BTREE,
  INDEX `idx_window_waiting_count`(`waiting_count` ASC) USING BTREE,
  CONSTRAINT `fk_window_doctor` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '挂号窗口表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of registration_window
-- ----------------------------
INSERT INTO `registration_window` VALUES ('176535674200979472', '176535580122376349', 10, '2025-12-10 16:52:22', '2025-12-10 16:52:22');

-- ----------------------------
-- Table structure for stock_warning
-- ----------------------------
DROP TABLE IF EXISTS `stock_warning`;
CREATE TABLE `stock_warning`  (
  `warning_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '预警ID',
  `medicine_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药品编号',
  `medicine_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '药品名称',
  `current_quantity` int NOT NULL COMMENT '当前库存',
  `warning_type` enum('LOW_STOCK','NEAR_EXPIRATION') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'LOW_STOCK' COMMENT '预警类型: LOW_STOCK-库存不足, NEAR_EXPIRATION-临近过期',
  `warning_message` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '预警信息',
  `warning_time` datetime NOT NULL COMMENT '预警时间',
  `is_handled` tinyint(1) NULL DEFAULT 0 COMMENT '是否处理: 0-未处理, 1-已处理',
  `handled_by` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '处理人',
  `handled_at` datetime NULL DEFAULT NULL COMMENT '处理时间',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`warning_id`) USING BTREE,
  INDEX `idx_warning_medicine`(`medicine_id` ASC) USING BTREE,
  INDEX `idx_warning_time_status`(`warning_time` DESC, `is_handled` ASC) USING BTREE,
  INDEX `idx_warning_type`(`warning_type` ASC) USING BTREE,
  INDEX `idx_warning_handled`(`is_handled` ASC) USING BTREE,
  INDEX `idx_warning_medicine_time`(`medicine_id` ASC, `warning_time` ASC) USING BTREE,
  CONSTRAINT `fk_warning_medicine` FOREIGN KEY (`medicine_id`) REFERENCES `medicine` (`medicine_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '库存预警表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of stock_warning
-- ----------------------------

-- ----------------------------
-- Table structure for treatment
-- ----------------------------
DROP TABLE IF EXISTS `treatment`;
CREATE TABLE `treatment`  (
  `treatment_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '治疗单号',
  `diagnosis_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '诊断记录编号',
  `doctor_id` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '医生ID',
  `treatment_method` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '治疗方法/设备',
  `treatment_time` datetime NOT NULL COMMENT '治疗时间',
  `treatment_period` int NULL DEFAULT NULL COMMENT '治疗周期(天)',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`treatment_id`) USING BTREE,
  INDEX `idx_treatment_diagnosis`(`diagnosis_id` ASC) USING BTREE,
  INDEX `idx_treatment_doctor`(`doctor_id` ASC) USING BTREE,
  INDEX `idx_treatment_time`(`treatment_time` ASC) USING BTREE,
  INDEX `idx_treatment_doctor_time`(`doctor_id` ASC, `treatment_time` ASC) USING BTREE,
  CONSTRAINT `fk_treatment_diagnosis` FOREIGN KEY (`diagnosis_id`) REFERENCES `diagnosis` (`diagnosis_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_treatment_doctor` FOREIGN KEY (`doctor_id`) REFERENCES `doctor` (`doctor_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '治疗记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of treatment
-- ----------------------------
INSERT INTO `treatment` VALUES ('176536149077896441', '176536129471065358', '176535580122376349', 'testtt', '2025-12-10 10:11:10', 10, '2025-12-10 18:11:30', '2025-12-10 18:11:30');

SET FOREIGN_KEY_CHECKS = 1;

DELIMITER //



-- 重新创建触发器
CREATE TRIGGER CheckStockAfterReduction AFTER UPDATE ON medicine
FOR EACH ROW
BEGIN
    -- 只有当库存减少且库存小于等于50时才生成预警
    IF NEW.quantity < OLD.quantity AND NEW.quantity <= 50 THEN
        -- 插入库存预警记录（使用更短的ID）
        INSERT INTO stock_warning (
            warning_id,
            medicine_id, 
            medicine_name, 
            current_quantity, 
            warning_type, 
            warning_message,
            warning_time,
            is_handled,
            created_at
        ) 
        VALUES (
            -- 缩短ID：WARN + Unix时间戳 + 随机数
            CONCAT('W', UNIX_TIMESTAMP(NOW()), LPAD(FLOOR(RAND() * 1000), 3, '0')),
            NEW.medicine_id, 
            NEW.medicine_name, 
            NEW.quantity, 
            'LOW_STOCK',
            CONCAT('库存不足预警，当前库存：', NEW.quantity),
            NOW(),
            0,
            NOW()
        );
    END IF;
END//

DELIMITER ;

-- 第四步：准备测试数据
-- 1. 先创建一个测试药厂
INSERT INTO pharmaceutical_factory (
    factory_id,
    factory_name,
    manager,
    address,
    qualification_level,
    phone_number
) VALUES (
    'TEST_FACTORY',
    '测试药厂有限公司',
    '张经理',
    '测试市测试区测试路123号',
    3,
    '13800138000'
);

-- 2. 插入一个测试药品，初始库存为80（高于预警线50）
INSERT INTO medicine (
    medicine_id,
    medicine_name,
    quantity,
    is_otc,
    production_date,
    expiration_date,
    price,
    factory_id
) VALUES (
    'TEST001',
    '测试药品A',
    80,  -- 初始库存80，高于预警线
    1,
    '2025-01-01',
    '2026-12-31',
    25.50,
    'TEST_FACTORY'
);

-- 查看插入的测试药品
SELECT '测试药品初始状态:' as '测试阶段',
       medicine_id,
       medicine_name,
       quantity as '当前库存'
FROM medicine WHERE medicine_id = 'TEST001';

-- 检查当前预警记录
SELECT COUNT(*) as '当前预警记录数' 
FROM stock_warning WHERE medicine_id = 'TEST001';

-- 第五步：开始测试触发器
-- -------------------------------------------------------------
-- 测试场景1：库存从80减少到60（不触发，因为 >50）
-- -------------------------------------------------------------
SELECT '\n--- 测试场景1：80 → 60（应该不触发预警） ---' as '';

UPDATE medicine 
SET quantity = 60 
WHERE medicine_id = 'TEST001';

SELECT '更新后库存:' as '', quantity 
FROM medicine WHERE medicine_id = 'TEST001';

SELECT '预警记录数:' as '', 
       (SELECT COUNT(*) FROM stock_warning WHERE medicine_id = 'TEST001') as '数量',
       CASE 
           WHEN (SELECT COUNT(*) FROM stock_warning WHERE medicine_id = 'TEST001') = 0 
           THEN '正确：未触发预警'
           ELSE '错误：不应该触发预警'
       END as '结果';

-- -------------------------------------------------------------
-- 测试场景2：库存从60减少到45（应该触发预警）
-- -------------------------------------------------------------

SELECT '\n--- 测试场景2：60 → 45（应该触发预警） ---' as '';

UPDATE medicine 
SET quantity = 45 
WHERE medicine_id = 'TEST001';

SELECT '更新后库存:' as '', quantity 
FROM medicine WHERE medicine_id = 'TEST001';

SELECT '预警记录数:' as '', 
       (SELECT COUNT(*) FROM stock_warning WHERE medicine_id = 'TEST001') as '数量',
       CASE 
           WHEN (SELECT COUNT(*) FROM stock_warning WHERE medicine_id = 'TEST001') = 1 
           THEN '正确：已触发预警'
           ELSE '错误：应该触发预警'
       END as '结果';


