-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.13-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para plancuentas
CREATE DATABASE IF NOT EXISTS `plancuentas` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `plancuentas`;

-- Volcando estructura para tabla plancuentas.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla plancuentas.grupo: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`id`, `descripcion`) VALUES
	(1, 'Activo'),
	(2, 'Pasivo'),
	(3, 'Patrimonio'),
	(4, 'Ingreso');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla plancuentas.plancuenta
CREATE TABLE IF NOT EXISTS `plancuenta` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Codigo` varchar(50) NOT NULL DEFAULT '',
  `grupo` int(11) NOT NULL,
  `Descripcion` varchar(100) DEFAULT NULL,
  `Naturaleza` varchar(50) DEFAULT NULL,
  `Estado` tinyint(50) NOT NULL,
  KEY `Id` (`Id`),
  KEY `grupo` (`grupo`),
  CONSTRAINT `FK_plancuenta_grupo` FOREIGN KEY (`grupo`) REFERENCES `grupo` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla plancuentas.plancuenta: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `plancuenta` DISABLE KEYS */;
INSERT INTO `plancuenta` (`Id`, `Codigo`, `grupo`, `Descripcion`, `Naturaleza`, `Estado`) VALUES
	(1, '1', 1, 'caja', 'D', 1),
	(2, '02', 1, 'banco', 'D', 1),
	(3, '03', 2, 'cuenta por pagar', 'A', 1),
	(4, '04', 3, 'Capital Contable', 'A', 1),
	(5, '05', 4, 'Ventas', 'A', 1),
	(6, '06', 4, 'Compras', 'D', 1),
	(8, '07', 4, 'Arriendo', 'D', 0);
/*!40000 ALTER TABLE `plancuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
